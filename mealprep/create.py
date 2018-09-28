from flask import (Blueprint, flash, g, redirect, render_template,
                   request, url_for, session)
from werkzeug.exceptions import abort
import mealprep.selection as Selection
import mealprep.storage as Storage

bp = Blueprint('create', __name__)


@bp.route('/')
def index():
    return render_template('foodlist/index.html')

@bp.route('/create', methods=('GET', 'POST'))
def create_list():
    if request.method == 'POST':
        # these requests are not working, storing variables as None
#        day_to_start_on = request.form['day_to_start_on']
        day_to_start_on = 'Tuesday'
        days_to_plan_for = request.form['days_to_plan_for']
        error = None
        session['day_to_start_on'] = day_to_start_on
        if not day_to_start_on:
            error = 'Day to start on is required.'
        elif not days_to_plan_for:
            error = 'Number of days is required.'
            
        if error is not None:
            flash(error)
        else:
            # run code to generate table to fill with meals
            recipe_df = Storage.read_recipe_storage()
            # dataframe that contains days with meals for each to be 
            # populated
            days_for_meal_prep = Selection.recipe_selection(
                    recipe_df, day_to_start_on, days_to_plan_for)
            session['days_for_meal_prep'] = days_for_meal_prep
    return render_template('foodlist/create.html')

@bp.route('/add', methods=('GET', 'POST'))
def add_recipe():
    return render_template('foodlist/add.html')

@bp.route('/select', methods=('GET', 'POST'))
def select_recipes():
    day_to_start_on = session.get('day_to_start_on')
    # days_for_meal_prep is being stored as nonetype
    days_for_meal_prep = session.get('days_for_meal_prep')
    flash(day_to_start_on)
    flash(days_for_meal_prep)
    # figure out how to display info from days_for_meal_prep here
    return render_template('/foodlist/selection.html', meals=[1, 1, 1])
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
        # add check to make sure start_day is valid
        start_day = request.form['start_day']
        number_days = request.form['number_days']
        error = None
        
        if not start_day:
            error = 'Day to start on is required.'
        elif not number_days:
            error = 'Number of days is required.'
            
        if error is not None:
            flash(error)
        else:
            # opens excel storage and outputs contents into dataframe
            recipe_df = Storage.read_recipe_storage()
            # create list of days to pick recipes for
            days_for_meal_prep = Selection.recipe_selection( 
                    recipe_df, start_day, number_days)
            session['days_for_meal_prep'] = days_for_meal_prep
            return redirect(url_for('create.select_recipes'))

    return render_template('foodlist/create.html')

@bp.route('/add', methods=('GET', 'POST'))
def add_recipe():
    return render_template('foodlist/add.html')

@bp.route('/select', methods=('GET', 'POST'))
def select_recipes():
    days_for_meal_prep = session.get('days_for_meal_prep')
    meals = ['Breakfast', 'Lunch', 'Dinner']
    recipe_df = Storage.read_recipe_storage()
    recipe_names = Storage.add_recipe_names_to_list(recipe_df)
    # get recipe_meals and store them and recipe_names as key:value pairs
    # key being the meal, that way can loop through dictionary and pull
    # out recipe_name values with correct meal key
    meal_served = Selection.output_recipe_meal_served(
            recipe_df, recipe_names)
    recipe_with_meal = dict(zip(recipe_names, meal_served))
    if request.method == 'POST':
        # get all values from drop downs and store as list
        picked_recipes = request.form.getlist('select_recipes')
        # pair recipes_picked with day_and_meal in dictionary
        day_and_meal = []
        for day in days_for_meal_prep:
            for meal in meals:
                day_and_meal.append(day + meal)
        day_meal_recipe = dict(zip(day_and_meal, picked_recipes))
        session['picked_recipes'] = picked_recipes
        session['day_meal_recipe'] = day_meal_recipe
        error = None
        
        if error is not None:
            flash(error)
        else:
            return redirect(url_for('create.grocery_list'))
    return render_template('/foodlist/selection.html', meals=meals,
                           days=days_for_meal_prep, recipes=recipe_with_meal)
    
@bp.route('/grocerylist', methods=('GET', 'POST'))
def grocery_list():
    picked_recipes = session.get('picked_recipes')
    return render_template('/foodlist/grocerylist.html',
                           picked_recipes=picked_recipes)
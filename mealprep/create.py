from flask import (Blueprint, flash, g, redirect, render_template,
                   request, url_for, session)
from werkzeug.exceptions import abort
from mealprep.db import get_db
import mealprep.selection as Selection
import mealprep.storage as Storage
import mealprep.CreateGroceryList as CreateGroceryList
import mealprep.EnterNewRecipe as EnterNewRecipe
import mealprep.ParseRecipe as ParseRecipe

bp = Blueprint('create', __name__)


@bp.route('/')
def index():
#    db = get_db()
#    recipes = db.execute(
#            'SELECT recipe_name, meal_served, serving_size,'
#            ' recipe_ingredients, recipe_measurements, recipe_amounts'
#            ).fetchall()
    return render_template('foodlist/index.html')

@bp.route('/create', methods=('GET', 'POST'))
def create_list():
    if request.method == 'POST':
        start_day = request.form['start_day'].capitalize()
        number_days = request.form['number_days']
        error = check_create_input_for_errors(start_day, number_days)
        # this is outside of error checking function to avoid having
        # to return error and number_days
        try:
            number_days = int(number_days)
        except ValueError:
            error = 'Number of days must be a number.'
            
        if error is not None:
            flash(error)
        else:
            # create list of days to pick recipes for
            days_for_meal_prep = Selection.days_to_plan_for( 
                    start_day, number_days)
            session['days_for_meal_prep'] = days_for_meal_prep
            return redirect(url_for('create.select_recipes'))

    return render_template('foodlist/create.html')

@bp.route('/add', methods=('GET', 'POST'))
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name'].capitalize()
        meal_served = request.form['meal_served'].capitalize()
        serving_size = request.form['serving_size']
        ingredient_info = request.form['ingredient_info']
        #ingredient_info is string in same format that is entered into text area
        #split ingredient info into amount, measurement, name for each ingredient
        recipe_info = ParseRecipe.parse_ingredient_info(ingredient_info)
        db = get_db()
        db.execute(
                'INSERT INTO recipe'
                ' (recipe_name, meal_served, serving_size)'
                ' VALUES (?, ?, ?)',
                (recipe_name, meal_served, serving_size))
        for ingredient in recipe_info.ingredients:
            ingredient_index = recipe_info.ingredients.index(ingredient)
            measurement = recipe_info.measurements[ingredient_index]
            amount = recipe_info.amounts[ingredient_index]
            # change this to be a one to many (one recipe to many ingredients)
            # relationship
            db.execute(
                    'INSERT INTO ingredient'
                    ' (recipe_id, ingredient, measurement, amount)'
                    ' VALUES (?, ?, ?)',
                    (recipe(id), ingredient, measurement, amount))
        db.commit()
        return redirect(url_for('create.index'))
    return render_template('foodlist/add.html')

@bp.route('/select', methods=('GET', 'POST'))
def select_recipes():
    days_for_meal_prep = session.get('days_for_meal_prep')
    meals = ['Breakfast', 'Lunch', 'Dinner']
    session['meals'] = meals
    db = get_db()
    recipes = db.execute(
            'SELECT recipe_name, meal_served, serving_size'
            ' FROM recipe').fetchall()
    if request.method == 'POST':
        picked_recipes = request.form.getlist('select_recipes')
        day_and_meal = []
        for day in days_for_meal_prep:
            for meal in meals:
                day_and_meal.append([day])
        session['day_and_meal'] = day_and_meal
        session['picked_recipes'] = picked_recipes
#        session['recipe_plans'] = recipe_plans
        error = None
        
        if error is not None:
            flash(error)
        else:
            return redirect(url_for('create.grocery_list'))
    return render_template('/foodlist/selection.html', meals=meals,
                           days=days_for_meal_prep, recipes=recipes)
    
@bp.route('/grocerylist', methods=('GET', 'POST'))
def grocery_list():
    # CHANGE THIS TO BE SQL BASED
    db = get_db()
    recipes = db.execute(
            'SELECT recipe_name, meal_served, serving_size'
            ' FROM recipe').fetchall()
    days_for_meal_prep = session.get('days_for_meal_prep')
    picked_recipes = session.get('picked_recipes')
#    recipe_plans = session.get('recipe_plans')
    meals = session.get('meals')
    day_and_meal = session.get('day_and_meal')
    grocery_df = CreateGroceryList.create_grocery_list(
            recipes, picked_recipes)
    grocery_list = []
    ingredient_names = grocery_df['Name'].tolist()
    ingredient_amount = grocery_df['Amount'].tolist()
    # add check to see if measurement is typical unit of measurement (ie cup)
    # if it is, round to eigths? if not, round to single digit
    ingredient_measurements = grocery_df['Measurement'].tolist()
    # zip together lists and iterate over them to combine elements at same index
    # from each list as string into combined list
    for name, amount, measurement in zip(ingredient_names, ingredient_amount,
                                         ingredient_measurements):
        ingredient_info = ("%(name)s: %(amount)s %(measurement)s" % {"name":name,
                   "amount":amount, "measurement":measurement})
        ingredient_info = ingredient_info.rstrip()
        grocery_list.append(ingredient_info)
    #this isn't used if grocery_list is used
    grocery_string = ", ".join(grocery_list)
    # round up amounts in grocery_list or before
    # add option to save grocery_list using OutputGroceryList.output_grocery_list(grocery_df)
    return render_template('/foodlist/grocerylist.html',
                           grocery_list=grocery_list,
                           days=days_for_meal_prep,
                           meals=meals,
                           recipes=picked_recipes)
    
def check_create_input_for_errors(start_day, number_days):        
    valid_days = ("Sunday", "Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday")
    error = None
    
    if not start_day:
        error = 'Day to start on is required.'
    elif start_day not in valid_days:
        error = 'That is not a valid day.'
    elif not number_days:
        error = 'Number of days is required.'
    return error

#class Recipe():
#    
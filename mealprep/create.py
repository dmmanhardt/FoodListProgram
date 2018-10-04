from flask import (Blueprint, flash, g, redirect, render_template,
                   request, url_for, session)
from werkzeug.exceptions import abort
import mealprep.selection as Selection
import mealprep.storage as Storage
import mealprep.CreateGroceryList as CreateGroceryList

bp = Blueprint('create', __name__)


@bp.route('/')
def index():
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
    # function to add new recipes to storage is not implemented yet
    return render_template('foodlist/add.html')

@bp.route('/select', methods=('GET', 'POST'))
def select_recipes():
    days_for_meal_prep = session.get('days_for_meal_prep')
    meals = ['Breakfast', 'Lunch', 'Dinner']
    session['meals'] = meals
    recipe_df = Storage.read_recipe_storage()
    recipe_names = Storage.add_recipe_names_to_list(recipe_df)
    # get recipe_meals and store them and recipe_names as key:value pairs
    # key being the meal, that way can loop through dictionary and pull
    # out recipe_name values with correct meal key
    meal_served = Selection.output_recipe_meal_served(
            recipe_df, recipe_names)
    recipe_with_meal = dict(zip(recipe_names, meal_served))
    if request.method == 'POST':
        picked_recipes = request.form.getlist('select_recipes')
        day_and_meal = []
        for day in days_for_meal_prep:
            for meal in meals:
                day_and_meal.append([day])        
        day_meal_recipe = zip(day_and_meal, picked_recipes)
        recipe_plans = []
        for day, recipe in day_meal_recipe:
            day.append(recipe)
            recipe_plans.append(day)
        session['day_and_meal'] = day_and_meal
        session['picked_recipes'] = picked_recipes
        session['recipe_plans'] = recipe_plans
        error = None
        
        if error is not None:
            flash(error)
        else:
            return redirect(url_for('create.grocery_list'))
    return render_template('/foodlist/selection.html', meals=meals,
                           days=days_for_meal_prep, recipes=recipe_with_meal)
    
@bp.route('/grocerylist', methods=('GET', 'POST'))
def grocery_list():
    recipe_df = Storage.read_recipe_storage()
    days_for_meal_prep = session.get('days_for_meal_prep')
    picked_recipes = session.get('picked_recipes')
    recipe_plans = session.get('recipe_plans')
    meals = session.get('meals')
    day_and_meal = session.get('day_and_meal')
    grocery_df = CreateGroceryList.create_grocery_list(
            recipe_df, picked_recipes)
    grocery_list = []
    ingredient_names = grocery_df['Name'].tolist()
    ingredient_amount = grocery_df['Amount'].tolist()
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
    # figure out how to display table with day/meal picks
    # display as breakfast   lunch   dinner
    #     day    recipe      recipe  recipe
    # create dataframe and display that?
    # or in html, create cell for recipe and pop it from dictionary
    # add option to save grocery_list using OutputGroceryList.output_grocery_list(grocery_df)
    return render_template('/foodlist/grocerylist.html',
                           grocery_list=grocery_list,
                           days=day_and_meal,
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
from flask import (Blueprint, flash, redirect, render_template,
                   request, url_for, session, jsonify)
from mealprep.db import get_db
import numpy as np
import mealprep.selection as Selection
import mealprep.CreateGroceryList as CreateGroceryList
import mealprep.ParseRecipe as ParseRecipe
import datetime

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
        print("in add_recipe")
        recipe_to_add_info = request.get_json()
        recipe_name = recipe_to_add_info['recipeName']
        meal_served = recipe_to_add_info['mealServed']
        serving_size = recipe_to_add_info['servingSize']
        ingredient_info = recipe_to_add_info['ingredientInfo']
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
            db.execute(
                    'INSERT INTO ingredient'
                    ' (recipe_id, ingredient, measurement, amount)'
                    ' VALUES ((SELECT id from recipe WHERE recipe_name=?), ?, ?, ?)',
                    (recipe_name, ingredient, measurement, amount))
        db.commit()
    return jsonify("success")

@bp.route('/edit', methods=('GET', 'POST'))
def select_recipe_to_edit():
    if request.method == 'POST':
        ingredient_list = []
        recipe_id = request.get_json()
        # fetch ingredient info from db based on recipe_id
        # provided by client
        ingredient_info = select_ingredient_info(recipe_id)
        for ingredient in ingredient_info:
            ingredient = Ingredient(ingredient['recipe_id'],
                            ingredient['id'],
                            ingredient['ingredient'], 
                            ingredient['measurement'],
                            ingredient['amount'])
            ingredient_list.append(ingredient)
        # returns list of objects for each recipe
        return jsonify([i.serialize() for i in ingredient_list])

# @bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@bp.route('/edit_recipe', methods=('GET', 'POST'))
def edit_recipe():
    if request.method == 'POST':
        recipe_info_to_be_updated = request.get_json()
        meal_served = recipe_info_to_be_updated['mealServed']
        recipe_ID = recipe_info_to_be_updated['recipeID']
        recipe_name = recipe_info_to_be_updated['recipeName']
        serving_size = recipe_info_to_be_updated['servingSize']
        ingredient_info = recipe_info_to_be_updated['ingredientInfo']
        # create ingredient object for each ingredient passed in ingredient_info
        ingredient_list = []
        for ingredient in ingredient_info:
            ingredient = Ingredient(recipe_ID,
                                    ingredient['ingredientID'],
                                    ingredient['name'],
                                    ingredient['measurement'],
                                    ingredient['amount']
                                    )
            ingredient_list.append(ingredient)
        update_recipe(recipe_ID, recipe_name, meal_served, serving_size)
        update_ingredient_info(ingredient_list, recipe_ID)
        print(ingredient_info)
        return jsonify("success")

@bp.route('/delete_recipe', methods=('GET', 'POST'))
def delete_recipe():
    if request.method =='POST':
        recipe_to_be_deleted = request.get_json()
        delete_recipe_from_db(recipe_to_be_deleted)
        return jsonify("success")

@bp.route('/select', methods=('GET', 'POST'))
def fetch_recipes():
    recipe_list = []
    if request.method == 'GET':
        db = get_db()
        recipes = db.execute(
                'SELECT id, recipe_name, meal_served, serving_size'
                ' FROM recipe').fetchall()
        # create class object for each recipe retrieved from db
        for recipe in recipes:
            recipe = Recipe(recipe['id'],
                            recipe['recipe_name'],
                            recipe['meal_served'], 
                            recipe['serving_size'])
            recipe_list.append(recipe)
        # returns list of objects for each recipe
        return jsonify([r.serialize() for r in recipe_list])

class Recipe():
    def __init__(self, recipe_id, recipe_name, meal_served, serving_size):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name.capitalize()
        self.meal_served = meal_served.capitalize()
        self.serving_size = serving_size
    def serialize(self):
        return {
            'recipeID': self.recipe_id,
            'recipeName': self.recipe_name,
            'mealServed': self.meal_served,
            'servingSize': self.serving_size,
        }

class Ingredient():
    def __init__(self, recipe_id, ingredient_id, name,
                measurement, amount):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.name = name
        self.measurement = measurement
        self.amount = amount
    def serialize(self):
        return {
            'recipeID': self.recipe_id,
            'ingredientID': self.ingredient_id,
            'name': self.name,
            'measurement': self.measurement,
            'amount': self.amount,
        }
        
@bp.route('/grocerylist', methods=('GET', 'POST'))
def grocery_list():
    if request.method == 'POST':
        picked_recipes = request.get_json()
        grocery_df = CreateGroceryList.create_grocery_list(picked_recipes)
        ingredient_names = grocery_df['Name'].tolist()
        ingredient_amounts = grocery_df['Amount'].tolist()
        ingredient_measurements = grocery_df['Measurement'].tolist()
        # zip together lists and iterate over them to combine elements at same index
        # from each list as string into combined list
        grocery_list = combine_ingredient_lists(ingredient_names,
                                                ingredient_amounts,
                                                ingredient_measurements)
        return jsonify(grocery_list)

# commit new ingredient_info from user into database for correct recipe
# and ingredient based on their respective id    
def update_ingredient_info(ingredient_list, recipe_ID):
    db = get_db()
    for ingredient in ingredient_list:
        ingredient_id = ingredient.ingredient_id
        amount = ingredient.amount
        ingredient_name = ingredient.name
        measurement = ingredient.measurement
        db.execute(
            'UPDATE ingredient SET ingredient = ?, measurement = ?,'
            ' amount = ? WHERE recipe_id = ? AND id = ?',
            (ingredient_name, measurement, amount, recipe_ID, ingredient_id)
        )
    db.commit()  

def delete_recipe_from_db(recipe_to_be_deleted):
    db = get_db()
    db.execute(
        'DELETE FROM recipe'
        ' WHERE id = ?',
        (recipe_to_be_deleted,)
    )     
    db.commit()

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

def select_recipe_info(id):
    db = get_db()
    recipe_info = db.execute(
        'SELECT id, recipe_name, meal_served, serving_size'
        ' FROM recipe'
        ' WHERE id = ?',
        (id,)).fetchone()
    return recipe_info

def select_ingredient_info(recipe_id):
    db = get_db()
    ingredient_info = db.execute(
        'SELECT r.recipe_name, r.meal_served, r.serving_size,'
        ' i.recipe_id, i.id, i.ingredient, i.measurement, i.amount'
        ' FROM recipe r'
        ' JOIN ingredient i ON r.id = i.recipe_id'
        ' WHERE r.id = ?',
        (recipe_id,)).fetchall()
    return ingredient_info

def create_ingredient_info_dict(
        ingredient_ids, amounts, ingredients, measurements):
    zipped_ingredient_info = zip(amounts, ingredients, measurements)
    ingredient_info_dict = dict(zip(
            ingredient_ids, zipped_ingredient_info))
    return ingredient_info_dict

def update_recipe(id, recipe_name, meal_served, serving_size):
    db = get_db()
    db.execute(
        'UPDATE recipe SET recipe_name = ?, meal_served = ?,'
        ' serving_size = ? WHERE id = ?',
        (recipe_name, meal_served, serving_size, id)
    )
    db.commit()

def combine_ingredient_lists(ingredient_names, ingredient_amounts,
                             ingredient_measurements):
    grocery_list = []
    for name, amount, measurement in zip(ingredient_names, 
                                         ingredient_amounts,
                                         ingredient_measurements):
        ingredient_info = ("%(name)s: %(amount)s %(measurement)s" % {
                "name":name, "amount":amount, "measurement":measurement})
        ingredient_info = ingredient_info.rstrip()
        grocery_list.append(ingredient_info)
    return grocery_list

# saves grocery_df to current working directory as text file
# figure out how to make this display save as dialog box to customize
# saving location
def save_as(grocery_df, picked_recipes):
    current_date = datetime.datetime.today().strftime("%Y-%m-%d")
#    test_file = open("grocerylist.txt", "a")
#    test_file.write(grocery_df.to_string())
#    test_file.close()
    filename = ("Grocery List %(date)s.txt" % {"date":current_date})
    np.savetxt(filename, grocery_df.values, fmt = "%s")
#    return send_file(test_file, as_attachment=True, attachment_filename="grocery_list.txt")
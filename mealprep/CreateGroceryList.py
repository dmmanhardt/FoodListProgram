# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:23:34 2018

@author: David
"""

import numpy as np
import pandas as pd
from mealprep.db import get_db

# uses picked recipes from selection.html and reads each recipes
# ingredients, outputs df with each ingredient's name, amount, and measurement
# based on the number of times each recipe was picked

def create_grocery_list(recipes, picked_recipes):
    initial_ingredient_info = [np.nan, np.nan, np.nan]
    # creates dataframe with a blank row in order to be able to append
    # to it for each recipe
    grocery_df = create_df(column_names = ["Name", "Measurement", "Amount"],
                            info_to_add = initial_ingredient_info,
                            name_df = "grocery_df")
    grocery_df.dropna(subset = ["Name"], inplace = True) 
    done_recipes = []
    for recipe in picked_recipes:
        if recipe == "none":
            continue
        elif recipe not in done_recipes:
            servings_needed = picked_recipes.count(recipe)
            db = get_db()
            # return ingredient information for recipe being looped over
            # as lists
            recipe_ingredient_names = create_recipe_info_list(
                    db, recipe, info="ingredient")
            recipe_ingredient_amount = create_recipe_info_list(
                    db, recipe, info="amount")
            recipe_ingredient_measurement = create_recipe_info_list(
                    db, recipe, info="measurement")
            # get recipe serving size from db
            recipe_serving_size = find_serving_size_from_db(db, recipe)              
            # convert the amount of each ingredient depending on the actual
            # servings needed
            if servings_needed != recipe_serving_size:
                serving_size_difference = (servings_needed / recipe_serving_size)
                recipe_ingredient_amount = load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference)
            grocery_df = add_info_to_grocery_df(grocery_df, 
                                                recipe_ingredient_names,
                                                recipe_ingredient_amount,
                                                recipe_ingredient_measurement)
            done_recipes.append(recipe) 
    grocery_df = sort_df(grocery_df) 
    grocery_df = change_column_types(grocery_df)
    return(grocery_df)
    
def create_recipe_info_list(db, recipe, info):
    # select info variable from db and return as cursor object
    ingredient_info = db.execute(
            'SELECT ingredient.recipe_id, ingredient.%s FROM recipe'
            ' JOIN ingredient ON recipe.id = ingredient.recipe_id'
            ' WHERE ingredient.recipe_id = '
            ' (SELECT id FROM recipe WHERE recipe_name = ?)' % (info),
            (recipe,))
    # add values from column of interest to list
    info_list = [row[info] for row in ingredient_info]
    return info_list

#returns serving size from db of recipe called
def find_serving_size_from_db(db, recipe):
    recipes_from_db = db.execute(
        'SELECT recipe_name, serving_size'
        ' FROM recipe')
    for db_recipe in recipes_from_db:
        if db_recipe['recipe_name'] == recipe:
            serving_size = db_recipe['serving_size']
    return serving_size

def create_df(column_names, info_to_add, name_df):
    name_df = pd.DataFrame([info_to_add], dtype='object')
    name_df.columns = column_names
    return name_df

def change_column_types(grocery_df):
    grocery_df = grocery_df.apply(pd.to_numeric, errors='ignore')
    return grocery_df       
        
# converts amounts to the correct amount needed based on serving_size_difference        
def load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference):
    recipe_ingredient_amount[:] = [(amount * serving_size_difference) for amount in recipe_ingredient_amount]
    return recipe_ingredient_amount   

def add_info_to_grocery_df(grocery_df, recipe_ingredient_names,
                           recipe_ingredient_amount, 
                           recipe_ingredient_measurement):
    for ingredient in recipe_ingredient_names:
        ingredient_index = recipe_ingredient_names.index(ingredient)
        ingredient_measurement = recipe_ingredient_measurement[ingredient_index]
        ingredient_amount = recipe_ingredient_amount[ingredient_index]
        ingredient_check = ingredient in grocery_df.Name.values
        if ingredient_check == True:
            stored_row = grocery_df.loc[grocery_df["Name"] == ingredient].index[0]
            stored_measurement = grocery_df.at[stored_row, "Measurement"]
            if ingredient_measurement == stored_measurement:
                stored_amount = grocery_df.loc[stored_row, "Amount"]
                grocery_df.at[stored_row, "Amount"] = (stored_amount + ingredient_amount)
            elif stored_measurement != recipe_ingredient_measurement[ingredient_index]:
                grocery_df = add_row_to_grocery_df(grocery_df, ingredient,
                                                   ingredient_measurement,
                                                   ingredient_amount)
        elif ingredient_check == False:
            grocery_df = add_row_to_grocery_df(grocery_df, ingredient,
                                               ingredient_measurement,
                                               ingredient_amount)
    return grocery_df
    
# adds ingredient info as a new row after last row of dataframe
def add_row_to_grocery_df(grocery_df, ingredient, ingredient_measurement,
                          ingredient_amount):
    grocery_df.loc[len(grocery_df)] = [
            ingredient, ingredient_measurement, ingredient_amount]
    return grocery_df

# sorts df by column "Name"
# this will allow same ingredients with different measurements
# to be near each other
def sort_df(grocery_df):
    grocery_df = grocery_df.sort_values(by='Name')
    return grocery_df 

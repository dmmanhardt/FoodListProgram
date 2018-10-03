# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:23:34 2018

@author: David
"""

import numpy as np
import pandas as pd
import mealprep.storage as Storage

# takes final dataframe with recipes for each meal, and reads each 
# recipes ingredients, outputs grocery list as text file with
# today's date in name.

def create_grocery_list(recipe_df, picked_recipes):
    initial_ingredient_info = [np.nan, np.nan, np.nan]
    # creates grocery_df with a blank row in order to be able to append
    # to it for each recipe
    grocery_df = create_df(column_names = ["Name", "Measurement", "Amount"],
                            info_to_add = initial_ingredient_info,
                            name_df = "grocery_df")
    # numpy is throwing a future warning somewhere, not sure from where
    grocery_df.dropna(subset = ["Name"], inplace = True) 
    done_recipes = []
    for recipe in picked_recipes:
        if recipe == "none":
            continue
        elif recipe not in done_recipes:
            servings_needed = picked_recipes.count(recipe)
            print(("%(recipe)s needs %(serving)s servings") % {
                    "recipe":recipe, "serving":servings_needed})
            (recipe_serving_size, recipe_ingredient_names, 
            recipe_ingredient_amount, recipe_ingredient_measurement) = Storage.read_recipe_information(recipe_df, recipe_name = recipe)
            print(("recipe serving size = %(size)i") % {"size":recipe_serving_size})
        # find and unpack the correct ingredient info for the recipe
            if servings_needed != recipe_serving_size:
                serving_size_difference = (servings_needed / recipe_serving_size)
                recipe_ingredient_amount = load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference)
            else:
                recipe_ingredient_amount = unpack_ingredient_amount(*recipe_ingredient_amount)
            recipe_ingredient_names = unpack_ingredient_names(*recipe_ingredient_names)
            recipe_ingredient_measurement = unpack_ingredient_measurement(*recipe_ingredient_measurement)
            # add info for ingredient to grocery_df
            grocery_df = add_info_to_grocery_df(grocery_df, 
                                                recipe_ingredient_names,
                                                recipe_ingredient_amount,
                                                recipe_ingredient_measurement)
            done_recipes.append(recipe) 
            print(done_recipes)
    grocery_df = sort_df(grocery_df) 
    grocery_df = change_column_types(grocery_df)
    return(grocery_df)
                

def create_df(column_names, info_to_add, name_df):
    name_df = pd.DataFrame([info_to_add], dtype='object')
    name_df.columns = column_names
    return name_df

def change_column_types(grocery_df):
    grocery_df = grocery_df.apply(pd.to_numeric, errors='ignore')
    return grocery_df

# unpacks items in recipe_ingredient_amount and returns them as a list of ints

def unpack_ingredient_amount(recipe_ingredient_amount):
    recipe_ingredient_amount = [float(amount) if "." in amount else 
                                int(amount) for amount in 
                                recipe_ingredient_amount.split(",")]
    return recipe_ingredient_amount        
        
# converts amounts to the correct amount needed based on serving_size_difference
        
def load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference):
    recipe_ingredient_amount = unpack_ingredient_amount(*recipe_ingredient_amount)
    recipe_ingredient_amount[:] = [(amount * serving_size_difference) for amount in recipe_ingredient_amount]
    return recipe_ingredient_amount   

def unpack_ingredient_names(recipe_ingredient_names):
    recipe_ingredient_names = [str(name) for name in recipe_ingredient_names.split(", ")]
    return recipe_ingredient_names

def unpack_ingredient_measurement(recipe_ingredient_measurement):
    recipe_ingredient_measurement = [str(measurement) for measurement in recipe_ingredient_measurement.split(", ")]
    return recipe_ingredient_measurement

def add_info_to_grocery_df(grocery_df, recipe_ingredient_names,
                           recipe_ingredient_amount, 
                           recipe_ingredient_measurement):
    for ingredient in recipe_ingredient_names:
        ingredient_index = recipe_ingredient_names.index(ingredient)
        ingredient_measurement = recipe_ingredient_measurement[ingredient_index]
        ingredient_amount = recipe_ingredient_amount[ingredient_index]
# fix rounding of float64 here? all floats aren't super long here though
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
# amounts are being converted to large floats when adding to df,
# try fixing the df to be int when it is created?
    grocery_df.loc[len(grocery_df)] = [
            ingredient, ingredient_measurement, ingredient_amount]
    return grocery_df

# sorts by "Name" sorts along with values in the other columns in the same row
# this will allow same ingredients with different measurements
# to be near each other
def sort_df(grocery_df):
    grocery_df = grocery_df.sort_values(by='Name')
    return grocery_df 

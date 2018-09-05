# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:08:25 2018

@author: MANHARDTD
"""

import pandas as pd
import os
        
# DATABASE ATTEMPT
# read recipe_storage excel file and grab recipe names and populate recipe_names list
# if a recipe is picked, then grab the rest of the info and populate the lists

# reads csv file and returns output as dataframe

def read_recipe_storage():
    file = "recipe_storage.csv"
    directory = os.path.dirname(os.path.realpath(file))
    file_to_open = directory + "\\" + file
    recipe_df = pd.read_csv(file_to_open, skipinitialspace = True)
    return recipe_df

# outputs recipe names to local variable as list

def add_recipe_names_to_list(recipe_df):
    recipe_names = []
    for recipe in recipe_df["Recipe Name"]:
        recipe_names.append(recipe)
    return recipe_names

def add_meal_served_to_list(recipe_df, recipe_name):
    recipe_row = output_recipe_row(recipe_df, recipe_name)
    recipe_meal = recipe_df.at[recipe_row, "Meal Served"]
    return recipe_meal
    
def output_recipe_row(recipe_df, recipe_name):
    recipe_row = recipe_df.loc[recipe_df["Recipe Name"] == recipe_name].index[0]
    return recipe_row

# takes info from .csv file and outputs info into lists, assumes
# all corresponding info is at same row

def read_recipe_information(recipe_df, recipe_name):
    recipe_ingredient_names = []
    recipe_ingredient_amount = []
    recipe_ingredient_measurement = []
    recipe_row = output_recipe_row(recipe_df, recipe_name)
    recipe_serving_size = recipe_df.at[recipe_row, "Serving Size"]
    recipe_ingredient_names.append(recipe_df.at[recipe_row, "Ingredient Names"])
    recipe_ingredient_amount.append(recipe_df.at[recipe_row, "Ingredient Amount"])
    recipe_ingredient_measurement.append(recipe_df.at[recipe_row, "Ingredient Measurement"]) 
    return (recipe_serving_size, recipe_ingredient_names, 
            recipe_ingredient_amount, recipe_ingredient_measurement)
    


def output_recipe_storage():
    recipe_df = pd.df({"Recipe Name" : recipe_names, 
                       "Serving Size" : recipe_serving_size, 
                       "Ingredient Names" : recipe_ingredient_names, 
                       "Ingredient Amount" : recipe_ingredient_amount, 
                       "Ingredient Measurement" : recipe_ingredient_measurement})
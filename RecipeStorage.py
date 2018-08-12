# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:08:25 2018

@author: MANHARDTD
"""

import pickle
import pandas as pd
import os

# recipe storage format = ["recipe_name: (ingredient_name: ingredient_amount: measurement, ingredient_name: ingredient_amount: measurement, etc)"]
# Ingredient class needs to be inside Recipe class? so that it is associated with the recipe
class Recipe(object):
    def __init__(self, name, ingredients, serving_size):
        self.name = name
        self.ingredients = ingredients
        self.serving_size = serving_size

class Ingredient(object):
    def __init__(self, name, amount, measurement):
        self.amount = amount
        self.measurement = measurement

# PICKLE ATTEMPT       
#with open('recipe_storage.pkl', 'wb') as output:
#    recipe1 = Recipe("steak and potatoes", "1 lb steak, 2 whole potatoes, 1 stick butter", "2")
#    ingredient_count = 0
#    for ingredient in recipe1.ingredients:
#        ingredient_count += 1
#        ingredient_number = "ingredient{}".format(ingredient_count)
#        ingredient_number = Ingredient("steak", "1", "lb")
#        
#    pickle.dump(recipe1, output, pickle.HIGHEST_PROTOCOL)
#  
## open recipe_storage.pkl and read all recipes, store them to local variables      
#with open('recipe_storage.pkl', 'rb') as input:
#    # need to find out how to store recipe info to correct recipe name
#    recipe1 = pickle.load(input)
#    print(recipe1.name)
#    print(recipe1.serving_size)
#    
    
# LIST ATTEMPT        
# ingredients will be stored after input from user as 3 lists, ingredient_name, ingredient_amount, and ingredient_measurement
#steak_and_potatoes = Recipe()
#
#ingredient_list = ["steak", "potatoes"]
#
#
#def get_ingredients(recipe_name):
#    for ingredient in ingredient_list:
#        ingredient_name.ingredient = recipe_name.ingredient
#        # change input to recipe_name.ingredient.serving_amount and recipe_name.ingredient.measurement
#        recipe_name.ingredient = Ingredient(input("Serving amount? "), input("Measurement? "))
#        print(recipe_name.ingredient.amount, recipe_name.ingredient.measurement)
        
# DATABASE ATTEMPT
# read recipe_storage excel file and grab recipe names and populate recipe_names list
# if a recipe is picked, then grab the rest of the info and populate the lists
recipe_names = []
recipe_serving_size = []
recipe_ingredient_names = []
recipe_ingredient_amount = []
recipe_ingredient_measurement = []

# reads csv file and returns output as dataframe

def read_recipe_storage():
    file = "recipe_storage.csv"
    directory = os.path.dirname(os.path.realpath(file))
    file_to_open = directory + "\\" + file
    recipe_dataframe = pd.read_csv(file_to_open, skipinitialspace = True)
    return recipe_dataframe

# outputs recipe names to local variable as list

def add_recipe_names_to_list():
    recipe_dataframe = read_recipe_storage()
    for recipe in recipe_dataframe["Recipe Name"]:
        recipe_names.append(recipe)
    print(recipe_names)

def read_recipe_information(recipe_name):
    recipe_dataframe = read_recipe_storage()
    # find correct row
    recipe_row = recipe_dataframe.loc[recipe_dataframe["Recipe Name"] == recipe_name]
    
            

def output_recipe_storage():
    recipe_dataframe = pd.dataframe({"Recipe Name" : recipe_names, 
                       "Serving Size" : recipe_serving_size, 
                       "Ingredient Names" : recipe_ingredient_names, 
                       "Ingredient Amount" : recipe_ingredient_amount, 
                       "Ingredient Measurement" : recipe_ingredient_measurement})
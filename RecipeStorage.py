# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:08:25 2018

@author: MANHARDTD
"""

# create recipe_list from RecipeListFile.txt

def read_recipe_storage():
    recipe_list = []
    recipe_storage = open('RecipeListFile.txt')
    content = recipe_storage.readlines()
    recipe_storage.close()        
    for recipe in content:
        recipe_list.append(recipe)
    return recipe_list

# recipe storage format = ["recipe_name: (ingredient_name: ingredient_amount: measurement, ingredient_name: ingredient_amount: measurement, etc)"]
# Ingredient class needs to be inside Recipe class? so that it is associated with the recipe
class Recipe(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

class Ingredient(object):
    def __init__(self, amount, measurement):
        self.amount = amount
        self.measurement = measurement
        
# ingredients will be stored after input from user as 3 lists, ingredient_name, ingredient_amount, and ingredient_measurement
steak_and_potatoes = Recipe()

ingredient_list = ["steak", "potatoes"]


def get_ingredients(recipe_name):
    for ingredient in ingredient_list:
        ingredient_name.ingredient = recipe_name.ingredient
        # change input to recipe_name.ingredient.serving_amount and recipe_name.ingredient.measurement
        recipe_name.ingredient = Ingredient(input("Serving amount? "), input("Measurement? "))
        print(recipe_name.ingredient.amount, recipe_name.ingredient.measurement)
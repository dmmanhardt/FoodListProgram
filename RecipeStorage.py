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
    
class Recipe(object):
    pass

class Ingredient(object):
    def __init__(self, amount, measurement):
        self.amount = amount
        self.measurement = measurement
        
# ingredients will be stored after input from user as 3 lists, ingredient_name, ingredient_amount, and ingredient_measurement
steak_and_potatoes = Recipe()

ingredient_list = ["steak", "potatoes"]

for ingredient in ingredient_list:
    steak_and_potatoes.ingredient = Ingredient(input("Serving amount? "), input("Measurement? "))
    print(steak_and_potatoes.ingredient.amount, steak_and_potatoes.ingredient.measurement)
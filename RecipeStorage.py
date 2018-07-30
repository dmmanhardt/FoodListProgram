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
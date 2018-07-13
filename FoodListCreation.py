# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:38:12 2018

@author: MANHARDTD
"""

def food_list_creation():
    #main menu asks user if they want to enter a recipe, create a food list, or exit
    main_menu()
    
    #create array for each recipe, named as recipe and key as ingredient, value as serving size
    
    list_of_recipes_with_ingredients = (recipe1(ingredient(serving)), recipe2(ingredient(serving)))
    #promt user how many nights they want to make a list for
    days_needing_recipes()
    #loop menu prompt until # of nights is full of recipes
    #menu promping user what they want to do (see list of recipes, pick a recipe, exit)
    recipe_selection_menu()
    
    #list of recipes displays the names of all the recipes entered
    
    #picking a recipe shows the ingredient list and how many nights/servings it lasts for
    
        #ask how many servings/nights (which nights? possibly assign recipe to certain nights)
        
        #show ingredients for that many nights, eventually add to evernote or something similar
        
    #exit loop and program
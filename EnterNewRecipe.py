# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:35:58 2018

@author: MANHARDTD
"""

#prompt user for name of recipe and see if it already exists in RecipeList, if not, run AddNewRecipe()
def enter_new_recipe():
    recipe_list = read_recipe_storage()
    while  True:
        recipe_name = input("What is the name of the recipe? ")
        #check to see if the recipe is already stored in recipeList
        #and add the recipe to recipeList if it isn't, proceed to add
        #ingredients
        if recipe_name not in recipe_list:
            add_new_recipe(recipe_name)
            break
        else:
            print("There is already a recipe with that name.")
            
def add_new_recipe(recipe_name):
    print("Adding new recipe: ", recipe_name)
    recipe_list.append(recipe_name)
    define_serving_size(recipe_name)
    enter_ingredients(recipe_name)
    #once ingredients are entered, add recipes to RecipeStorage and close
    add_recipes_to_file(recipe_name)
    
def define_serving_size(recipe_name):
    serving_size = []
    serving_size.append(input("How many meals does this recipe serve for two people? "))
    
def enter_ingredients(recipe_name):
    print("We will now add the ingredients for", recipe_name, ", please enter each ingredient \
individually")
    ingredients = []
    #take ingredient name and add to list, will add amount later
    while True:
        ingredients_choice = input("Enter the name of the ingredient, \
if no more ingredients, type 'next': ")
        if ingredients_choice == "next":
            break
        else:
            ingredients.append(ingredients_choice)
            print("Your ingredients so far are: ", ingredients)
        
    #go through tuple and prompt user to add amount of each
    #how to do units?
    
#add new recipes to RecipeListFile and close file
def add_recipes_to_file(recipe_name):
        for recipe in recipe_list:
            if recipe not in 'RecipeListFile.txt':
                print('Adding ', recipe_name, 'to RecipeStorage.txt.')
                recipe_storage = open('RecipeListFile.txt', 'a')
                recipe_storage.write(recipe)
                recipe_storage.close()
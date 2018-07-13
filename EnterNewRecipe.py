# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:35:58 2018

@author: MANHARDTD
"""
#create recipe list text file? and store recipes there
#open file first and read contents, store to list in order to append recipes to list later if necessary
recipe_list = []
recipe_storage = open('RecipeListFile.txt')
content = recipe_storage.readlines()
recipe_storage.close()
    
for recipe in content:
    recipe_list.append(recipe)

#prompt user for name of recipe and see if it already exists in RecipeList, if not, run AddNewRecipe()
def enter_new_recipe():
    new_recipe_name = False
    while new_recipe_name == False:
        recipe_name = input("What is the name of the recipe? ")
        #check to see if the recipe is already stored in recipeList
        #and add the recipe to recipeList if it isn't, proceed to add
        #ingredients
        if recipe_name not in recipe_list:
            new_recipe_name = True
            add_new_recipe(recipe_name)
        else:
            print("There is already a recipe with that name.")
            
def add_new_recipe(recipe_name):
    print("Adding new recipe: ", recipe_name)
    recipe_list.append(recipe_name)
    #prompt user to enter how many days/servings the recipe is 
    #and assign that to a serving size variable
    define_serving_size(recipe_name)
    #store serving size in tuple? as ((recipeName, servingSize, Ingredients),(recipeName,etc))
    #StoreServingSize(ServingSize)
    #once recipe is named, ask for ingredients and add to a tuple
    enter_ingredients(recipe_name)
    #once ingredients are entered, add recipes to RecipeStorage and close
    add_recipes_to_file(recipe_name)
    
def define_serving_size(recipe_name):
    serving_size = input("How many meals does this recipe serve for two people? ")
    
    
def enter_ingredients(recipe_name):
    print("We will now add the ingredients for", recipe_name, ", please enter each ingredient \
individually")
    ingredients = []
    more_ingredients_to_add = True
    ingredient_number = 1
    #take ingredient name and add to list, will add amount later
    while more_ingredients_to_add == True:
        ingredients_choice = input("Enter the name of the ingredient, \
if no more ingredients, type 'next': ")
        if ingredients_choice == "next":
            more_ingredients_to_add = False
            break
        else:
            ingredients.append(ingredients_choice)
            ingredient_number += 1
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
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:35:58 2018

@author: MANHARDTD
"""
#create recipe list text file? and store recipes there
#open file first and read contents, store to list in order to append recipes to list later if necessary
RecipeList = []
RecipeStorage = open('RecipeListFile.txt')
content = RecipeStorage.readlines()
RecipeStorage.close()
    
for recipe in content:
    RecipeList.append(recipe)

#prompt user for name of recipe and see if it already exists in RecipeList, if not, run AddNewRecipe()
def EnterNewRecipe():
    newRecipeName = False
    while newRecipeName == False:
        RecipeName = input("What is the name of the recipe? ")
        #check to see if the recipe is already stored in recipeList
        #and add the recipe to recipeList if it isn't, proceed to add
        #ingredients
        if RecipeName not in RecipeList:
            newRecipeName = True
            AddNewRecipe(RecipeName)
        else:
            print("There is already a recipe with that name.")
            
def AddNewRecipe(RecipeName):
    print("Adding new recipe: ", RecipeName)
    RecipeList.append(RecipeName)
    #prompt user to enter how many days/servings the recipe is 
    #and assign that to a serving size variable
    DefineServingSize(RecipeName)
    #store serving size in tuple? as ((recipeName, servingSize, Ingredients),(recipeName,etc))
    #StoreServingSize(ServingSize)
    #once recipe is named, ask for ingredients and add to a tuple
    EnterIngredients(RecipeName)
    #once ingredients are entered, add recipes to RecipeStorage and close
    AddRecipesToFile(RecipeName)
    
def DefineServingSize(RecipeName):
    ServingSize = input("How many meals does this recipe serve for two people? ")
    
    
def EnterIngredients(RecipeName):
    print("We will now add the ingredients for", RecipeName, ", please enter each ingredient \
individually")
    Ingredients = []
    MoreIngredients = True
    ingredientNumber = 1
    #take ingredient name and add to list, will add amount later
    while MoreIngredients == True:
        IngredientsChoice = input("Enter the name of the ingredient, \
if no more ingredients, type 'next': ")
        if IngredientsChoice == "next":
            MoreIngredients = False
            break
        else:
            Ingredients.append(IngredientsChoice)
            ingredientNumber += 1
            print("Your ingredients so far are: ", Ingredients)
        
    #go through tuple and prompt user to add amount of each
    #how to do units?
    
#add new recipes to RecipeListFile and close file
def AddRecipesToFile(RecipeName):
        for recipe in RecipeList:
            if recipe not in 'RecipeListFile.txt':
                print('Adding ', RecipeName, 'to RecipeStorage.txt.')
                RecipeStorage = open('RecipeListFile.txt', 'a')
                RecipeStorage.write(recipe)
                RecipeStorage.close()
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:35:58 2018

@author: MANHARDTD
"""
#create recipe list text file? and store recipes there
import pickle
RecipeList = []
newfile = "RecipeStorage.pk"
with open(newfile, "wb") as RecipeStorage:
    pickle.dump(RecipeList, RecipeStorage)

#prompt user for name of recipe and create list named as input
#rename this function
def EnterNewRecipe():
    newRecipeName = False
    while newRecipeName == False:
        RecipeName = input("What is the name of the recipe? ")
        #check to see if the recipe is already stored in recipeList
        #and add the recipe to recipeList if it isn't, proceed to add
        #ingredients
        if RecipeName not in RecipeList:
            newRecipeName = True
            RecipeList.append(RecipeName)
            addNewRecipe(RecipeName)
        else:
            print("There is already a recipe with that name.")
            
def addNewRecipe(RecipeName):
    print("Adding new recipe: ", RecipeName)
    #prompt user to enter how many days/servings the recipe is 
    #and add assign that to a serving size variable
    ServingSize = input("How many meals does this recipe serve for two people? ")
    #store serving size in tuple? as ((recipeName, servingSize, Ingredients),(recipeName,etc))
    #StoreServingSize(ServingSize)
    #once recipe is named, ask for ingredients and add to a tuple
    print("We will now add the ingredients for", RecipeName, ", please enter each ingredient \
individually")
    EnterIngredients(RecipeName)
    
def EnterIngredients(RecipeName):
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
    
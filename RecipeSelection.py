# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:20:32 2018

@author: David
"""

import pandas as pd

breakfast_recipes = []
lunch_recipes = []
dinner_recipes = []

# main function that calls functions to select recipes for each day needed and append them to a dataframe

# recipe_list is undefined for now, need to create function to grab current recipes

recipe_names = add_recipe_names_to_list()

def recipe_selection():
    days_for_meal_prep = create_days_needing_recipes()
    print("We will now select recipes for", days_for_meal_prep)
    df = pd.DataFrame(columns = days_for_meal_prep)
    pick_meals_for_days(days_for_meal_prep, recipe_names)
    final_recipe_dataframe = add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes)    

# takes user selection of recipe for each meal in each day in days_for_meal_prep and outputs lists for each meal of the day
# COULD USE REFACTORING

def pick_meals_for_days(days_for_meal_prep, recipe_names):
    meals = ["breakfast", "lunch", "dinner"]
    for day in days_for_meal_prep:
        for meal in meals:
            while True:
                list_available_recipes(recipe_names)
                # take input and convert to int
                recipe_picked = int(input("What would you like for %(meal)s on %(day)s? "\
                                       % {'meal': meal, 'day': day}))
                if recipe_check(recipe_picked, recipe_names) == True:
                    break
                print("That is not a valid recipe, please enter a recipe")
            # adds 1 to recipe_picked int and converts to the actual name of the recipe
            recipe_picked = recipe_names[recipe_picked - 1]
            add_meal_picked_to_day(meal, recipe_picked)
    return breakfast_recipes, lunch_recipes, dinner_recipes

def list_available_recipes(recipe_names):
    print("Available recipes:")
    for recipe in recipe_names:
        count = (recipe_names.index(recipe) + 1)  
        print("%(count)s) %(recipe)s" % {"count": count, "recipe": recipe})

def recipe_check(recipe_picked, recipe_names):
    recipe_numbers = []
    for recipe in recipe_names:
        recipe_numbers.append(recipe_names.index(recipe) + 1)
    if recipe_picked in recipe_numbers:
        return True
    else:
        return False

def add_meal_picked_to_day(meal, recipe_picked):
    if meal == "breakfast":
        breakfast_recipes.append(recipe_picked)
    elif meal == "lunch":
        lunch_recipes.append(recipe_picked)
    elif meal == "dinner":
        dinner_recipes.append(recipe_picked)
    else:
        print("Error occurred appending recipe.")

    # add if statements:
    # if input = skip, add none to day and skip that day
        
def add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes):
    print("called add_recipes_to_dataframe")
    df = pd.DataFrame({"Days": days_for_meal_prep, "Breakfast": breakfast_recipes, "Lunch": lunch_recipes, "Dinner": dinner_recipes})
    return df
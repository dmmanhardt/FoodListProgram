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

recipe_list = ["none", "chicken"]

def recipe_selection():
    days_for_meal_prep = create_days_needing_recipes()
    print("We will now select recipes for ", days_for_meal_prep)
    df = pd.DataFrame(columns = days_for_meal_prep)
    print(df)
    pick_meals_for_days(days_for_meal_prep, recipe_list)
    final_recipe_dataframe = add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes)
    

# takes user selection of recipe for each meal in each day in days_for_meal_prep and outputs lists for each meal of the day

def pick_meals_for_days(days_for_meal_prep, recipe_list):
    meals = ["breakfast", "lunch", "dinner"]
    for day in days_for_meal_prep:
        for meal in meals:
            while True:
                recipe_picked = (input("What would you like for %(meal)s on " % {'meal': meal} + day + "? " ))
                if recipe_picked in recipe_list:
                    break
                print("That is not a valid recipe, please enter a recipe")
            add_meal_picked_to_day(meal, recipe_picked)
    return breakfast_recipes, lunch_recipes, dinner_recipes

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
    df = pd.DataFrame({"Days": days_for_meal_prep, "Breakfast": breakfast_recipes, "Lunch": lunch_recipes, "Dinner": dinner_recipes})
    print(df)
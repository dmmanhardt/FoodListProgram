# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:20:32 2018

@author: David
"""
import pandas as pd

def recipe_selection(days_for_meal_prep):
    print("We will now select recipes for ", days_for_meal_prep)
    df = pd.DataFrame(columns = days_for_meal_prep)
    print(df)
    return df

def pick_meals_for_days(days_for_meal_prep, recipe_list):
    breakfast_recipes = []
    lunch_recipes = []
    dinner_recipes = []
    meals = ["breakfast", "lunch", "dinner"]
    for day in days_for_meal_prep:
        for meal in meals:
            while True:
                recipe_picked = (input("What would you like for %(meal)s on " % {'meal': meal} + day + "? " ))
                if recipe_picked not in recipe_list:
                    print("That is not a valid recipe, please enter a recipe")
                break
            add_meal_picked_to_day(meal, recipe_picked)
    return breakfast_recipes, lunch_recipes, dinner_recipes

def add_meal_picked_to_day(meal, recipe_picked):
    print("called add_meal_picked_to_day which is not functional")
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
    # if input is not in list of recipes, ask to select new recipe
        
def add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes):
    df = pd.DataFrame({"Days": days_for_meal_prep, "Breakfast": breakfast_recipes, "Lunch": lunch_recipes, "Dinner": dinner_recipes})
    print(df)
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

def pick_meals_for_days(days_for_meal_prep):
    breakfast_recipes = []
    lunch_recipes = []
    dinner_recipes = []
    for day in days_for_meal_prep:
        breakfast_recipes.append(input("What would you like for breakfast on " + day + "? "))
        lunch_recipes.append(input("What would you like for lunch on " + day + "? "))
        dinner_recipes.append(input("What would you like for dinner on " + day + "? "))
        # add if statements:
        # if input = skip, add none to day and skip that day
        # if input is not in list of recipes, ask to select new recipe
    return breakfast_recipes, lunch_recipes, dinner_recipes
        
def add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes):
    df = pd.DataFrame({"Days": days_for_meal_prep, "Breakfast": breakfast_recipes, "Lunch": lunch_recipes, "Dinner": dinner_recipes})
    print(df)
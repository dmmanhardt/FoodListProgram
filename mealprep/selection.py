# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:20:32 2018

@author: David
"""

import pandas as pd
import mealprep.storage as Storage
import mealprep.DaysNeedingRecipes as DaysNeedingRecipes

# main function that calls functions to select recipes for each day needed and append them to a dataframe
def recipe_selection(recipe_df, day_to_start_on, days_to_plan_for):
    recipe_names = Storage.add_recipe_names_to_list(recipe_df)
    meal_served = output_recipe_meal_served(recipe_df, recipe_names)
    breakfast_recipes = []
    lunch_recipes = []
    dinner_recipes = []
    # takes user input and creates list of days starting at day_to_start_on
    # and adds days_to_plan_for number of days to it
    days_for_meal_prep = DaysNeedingRecipes.create_days_needing_recipes(
            day_to_start_on, days_to_plan_for)
    # creates a dataframe to store recipes picked
    df = pd.DataFrame(columns = days_for_meal_prep)
    # add meals picked to dataframe
    # CHANGE PICK MEALS FOR DAYS TO BE BROWSER BASED
    return days_for_meal_prep
#    pick_meals_for_days(days_for_meal_prep, recipe_names, meal_served, 
#                        breakfast_recipes, lunch_recipes, dinner_recipes)
#    final_recipe_dataframe = add_recipes_to_dataframe(days_for_meal_prep, breakfast_recipes, lunch_recipes, dinner_recipes)
#    return final_recipe_dataframe

def output_recipe_meal_served(recipe_df, recipe_names):
    meal_served = []
    for recipe_name in recipe_names:
        recipe_meal = Storage.add_meal_served_to_list(recipe_df, recipe_name)
        meal_served.append(recipe_meal)
    return meal_served

# takes user selection of recipe for each meal in each day in days_for_meal_prep and outputs lists for each meal of the day
# COULD USE REFACTORING

def pick_meals_for_days(days_for_meal_prep, recipe_names, meal_served,
                        breakfast_recipes, lunch_recipes, dinner_recipes):
    meals = ["breakfast", "lunch", "dinner"]
    for meal in meals:
        for day in days_for_meal_prep:
            while True:
                recipe_numbers = list_available_recipes(recipe_names, meal, meal_served)
                corresponding_recipes = list_corresponding_recipes(
                        recipe_names, meal, meal_served)
                recipe_picked = int(input("What would you like for %(meal)s on %(day)s? "\
                                       % {'meal': meal, 'day': day}))
                if recipe_check(recipe_picked, recipe_numbers) == True:
                    break
                print("That is not a valid recipe, please enter a recipe")
                # converts number picked back to corresponding recipe_name string
            recipe_picked = corresponding_recipes[recipe_picked - 1]
            add_meal_picked_to_day(meal, recipe_picked, breakfast_recipes,
                                   lunch_recipes, dinner_recipes)
    return breakfast_recipes, lunch_recipes, dinner_recipes

def list_recipe_meal(recipe_names, meal, meal_served, recipe):
    recipe_index = recipe_names.index(recipe)
    recipe_meal = meal_served[recipe_index].lower()
    return recipe_meal

def list_corresponding_recipes(recipe_names, meal, meal_served):
    corresponding_recipes = []
    for recipe in recipe_names:
        recipe_meal = list_recipe_meal(recipe_names, meal, meal_served,
                                       recipe)
        corresponding_recipes = add_corresponding_recipe(
                recipe_meal, meal, corresponding_recipes, recipe)
    return corresponding_recipes
            
def add_corresponding_recipe(recipe_meal, meal, corresponding_recipes,
                             recipe):
    if recipe_meal == meal:
        corresponding_recipes.append(recipe)
    return corresponding_recipes

def list_available_recipes(recipe_names, meal, meal_served):
    print("Available recipes:")
    number = 1
    recipe_numbers = []
    for recipe in recipe_names:
        recipe_index = recipe_names.index(recipe)
        recipe_meal = meal_served[recipe_index].lower()
        if recipe_meal == meal:  
            recipe_numbers = add_recipe_number(number, recipe_numbers)
            print("%(number)s) %(recipe)s" % {"number": number, "recipe": recipe})
            number += 1
    return recipe_numbers

def add_recipe_number(number, recipe_numbers):
    recipe_numbers.append(number)
    return recipe_numbers

def recipe_check(recipe_picked, recipe_numbers):
    if recipe_picked in recipe_numbers:
        return True
    else:
        return False

def add_meal_picked_to_day(meal, recipe_picked, breakfast_recipes,
                           lunch_recipes, dinner_recipes):
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
    final_recipe_dataframe = pd.DataFrame({"Days": days_for_meal_prep, "Breakfast": breakfast_recipes, "Lunch": lunch_recipes, "Dinner": dinner_recipes})
    return final_recipe_dataframe
    
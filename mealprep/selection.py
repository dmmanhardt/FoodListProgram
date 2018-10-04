# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:20:32 2018

@author: David
"""

import mealprep.storage as Storage

def days_to_plan_for(start_day, number_days):
    valid_days = ("Sunday", "Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday")
    index = valid_days.index(start_day)
    # doubling the list since before the script would not be able to 
    # loop over the list more than twice
    valid_days = valid_days * 2
    days_for_meal_prep = []
    days_for_meal_prep = (valid_days + valid_days)[index:index + number_days]
    return days_for_meal_prep

def output_recipe_meal_served(recipe_df, recipe_names):
    meal_served = []
    for recipe_name in recipe_names:
        recipe_meal = Storage.add_meal_served_to_list(recipe_df, recipe_name)
        meal_served.append(recipe_meal)
    return meal_served
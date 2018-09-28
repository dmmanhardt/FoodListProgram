# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:40 2018

@author: MANHARDTD
"""

# takes user input for the amount of days to plan recipes for, and creates a list with that number of days

def create_days_needing_recipes(day_to_start_on, days_to_plan_for):
    while True:
        try:
            number_of_days_to_plan_for = int(number_of_days_to_plan_for)
            break
        except:
            error = "Number of days to plan for must be an integer."
    valid_days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    while True:
        if day_to_start_on in valid_days:
            days_for_meal_prep = days_to_plan_for(day_to_start_on, valid_days, number_of_days_to_plan_for)
            return days_for_meal_prep
            break
        else:
            error = "Day to start on must be a valid day."
        break

def days_to_plan_for(day_to_start_on, valid_days, number_of_days_to_plan_for):
    index = valid_days.index(day_to_start_on)
    # doubling the list since before the script would not be able to loop over the list more than twice
    valid_days = valid_days * 2
    days_for_meal_prep = []
    days_for_meal_prep = (valid_days + valid_days)[index:index + number_of_days_to_plan_for]
    return days_for_meal_prep
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:40 2018

@author: MANHARDTD
"""

# takes user input for the amount of days to plan recipes for, and creates a list with that number of days

def create_days_needing_recipes(start_day, number_days):
    while True:
        try:
            number_days = int(number_days)
            break
        except:
            error = "Number of days to plan for must be an integer."
    valid_days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    while True:
        if start_day in valid_days:
            days_for_meal_prep = days_to_plan_for(start_day, valid_days, number_days)
            return days_for_meal_prep
            break
        else:
            error = "Day to start on must be a valid day."
        break

def days_to_plan_for(start_day, valid_days, number_days):
    index = valid_days.index(start_day)
    # doubling the list since before the script would not be able to loop over the list more than twice
    valid_days = valid_days * 2
    days_for_meal_prep = []
    days_for_meal_prep = (valid_days + valid_days)[index:index + number_days]
    return days_for_meal_prep
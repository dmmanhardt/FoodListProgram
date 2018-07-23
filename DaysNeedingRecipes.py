# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:40 2018

@author: MANHARDTD
"""

#takes user input for the amount of days to plan recipes for, and creates a list with that number of days
#or creates a variable for each day with breakfast, lunch, and dinner?

def create_days_needing_recipes():
    while True:
        number_of_days_to_plan_for = input("Type the number of days you want to make a list for as an integer: ")
        try:
            number_of_days_to_plan_for = int(number_of_days_to_plan_for)
            break
        except:
            print("That is not a valid input, please enter an integer.")
    valid_days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    while True:
        day_to_start_on = input("What day will the list start on? ").lower()
        if day_to_start_on in valid_days:
            days_to_plan_for(day_to_start_on, valid_days, number_of_days_to_plan_for)
            break
        else:
            print("That is not a valid day")
        break

def days_to_plan_for(day_to_start_on, valid_days, number_of_days_to_plan_for):
    index = valid_days.index(day_to_start_on)
    # doubling the list since before the script would not be able to loop over the list more than twice
    valid_days = valid_days * 2
    days_for_meal_prep = []
    days_for_meal_prep = (valid_days + valid_days)[index:index + number_of_days_to_plan_for]
    print(days_for_meal_prep)
    return days_for_meal_prep

def assign_meals_to_days(days_for_meal_prep):
    days_for_breakfast = days_for_meal_prep
    days_for_lunch = days_for_meal_prep
    days_for_dinner = days_for_meal_prep      
    return days_for_breakfast, days_for_lunch, days_for_dinner
    
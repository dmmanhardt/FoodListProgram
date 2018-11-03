# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:35:58 2018

@author: MANHARDTD
"""

import csv

# prompt user for name of recipe and see if it already exists in 
# recipe_names, if not, run add_new_recipe()
def enter_new_recipe(recipe_df):
    recipe_names = add_recipe_names_to_list(recipe_df)
    while  True:
        recipe_name = input("What is the name of the recipe? ")
        if recipe_name not in recipe_names:
            add_new_recipe(recipe_name, recipe_names)
            break
        else:
            print("There is already a recipe with that name.")
    
# has user input ingredient info and adds that info to the recipe 
# storage file
        
def add_new_recipe(recipe_name, recipe_names):
    print("Adding new recipe: ", recipe_name)
    serving_size = enter_serving_size(recipe_name)
    meal_served = enter_meal_served(recipe_name)
    ingredients = enter_ingredients(recipe_name)
    measurements = enter_measurements(ingredients)
    amounts = enter_amounts(ingredients)
    ingredients = convert_list_to_string(list_name=ingredients)
    measurements = convert_list_to_string(list_name=measurements)
    amounts = convert_list_to_string(list_name=amounts)
    add_recipes_to_file(recipe_name, recipe_names, meal_served, 
                        serving_size, ingredients, amounts, measurements)
    
    
def enter_serving_size(recipe_name):
    serving_size = int(input("How many meals does this recipe serve for two people? "))
    return serving_size

def enter_ingredients(recipe_name):
    print("We will now add the ingredients for %(name)s, please enter each ingredient \
individually" % {"name":recipe_name})
    ingredients = []
    #take ingredient name and add to list, will add amount later
    while True:
        ingredients_choice = input("Enter the name of the ingredient, \
if no more ingredients, type 'next': ")
        if ingredients_choice == "next":
            break
        else:
            ingredients.append(ingredients_choice)
            print("Your ingredients so far are: ", ingredients)
    return ingredients

def enter_measurements(ingredients):
    measurements = []
    print("We will now enter the measurement for each ingredient")
    for ingredient in ingredients:
        measurement = input(("Enter the measurement for %(ingredient)s, \
if no measurement, type 'skip'. ") % {"ingredient":ingredient})
        if measurement.lower() == 'skip':
            measurement = ""
        measurements.append(measurement)
    return measurements

def enter_amounts(ingredients):
    amounts = []
    print("We will now enter the amount for each ingredient")
    for ingredient in ingredients:
        amount = input(("Enter the amount for %(ingredient)s, if no \
amount, type 'skip'. ") % {"ingredient":ingredient})
        if amount.lower() == 'skip':
            amount = ""
        amounts.append(amount)
    return amounts

def enter_meal_served(recipe_name):
    while True:
        meal_input = input(("What meal is %(recipe)s usually served? \n\
1)Breakfast \n\
2)Lunch \n\
3)Dinner \n\
Your input: ") % {"recipe":recipe_name})
        if meal_input == "1":
            meal_served = "Breakfast"
            break
        elif meal_input == "2":
            meal_served = "Lunch"
            break
        elif meal_input == "3":
            meal_served = "Dinner"
            break
        else:
            print("That is not a valid option")
    return meal_served
    
#append info for new recipe to new row in recipe_storage.csv
    
#unpack ingredients, amounts, measurements before adding
    
def convert_list_to_string(list_name):
    list_name = ', '.join(list_name)
    return list_name
    
def add_recipes_to_file(recipe_name, recipe_names, meal_served, 
                        serving_size, ingredients, amounts, measurements):
    # double check to make sure recipe is not already in recipe_names
    if recipe_name not in recipe_names:
        print(('Adding %(name)s to recipe_storage.csv.') % {
                "name":recipe_name})
        with open("recipe_storage.csv", "a") as recipe_storage:
            info_writer = csv.writer(recipe_storage)
            # this adds them as lists, want them entered as strings
            info_to_write = [recipe_name, meal_served, serving_size,
                             ingredients, amounts, measurements]
            info_writer.writerow(info_to_write)
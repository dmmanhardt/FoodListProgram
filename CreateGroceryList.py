# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:23:34 2018

@author: David
"""

# takes final dataframe with recipes for each meal, and reads each recipes ingredients, outputs grocery list as text file with
# today's date in name

def create_grocery_list(final_recipe_dataframe):
    all_recipes = []
    final_ingredient_names = ['bacon']
    final_ingredient_amounts = [3.0]
    final_ingredient_measurements = ['slices']
    for recipe in final_recipe_dataframe.itertuples():
        all_recipes.append(recipe.Breakfast)
        all_recipes.append(recipe.Lunch)
        all_recipes.append(recipe.Dinner)
        done_recipes = []
        # create count for each unique recipe in each list
        for recipe in all_recipes:
            if recipe not in done_recipes:
                ingredient_names = []
                ingredient_amounts = []
                ingredient_measurements = []
                # MOVE THIS TO END OF FUNCTION ONCE COMPLETE
                done_recipes.append(recipe)
                servings_needed = all_recipes.count(recipe)
                print(("%(recipe)s needs %(serving)s servings") % {
                        "recipe":recipe, "serving":servings_needed})
            # read ingredient info for each unique recipe
                (recipe_serving_size, recipe_ingredient_names, 
                recipe_ingredient_amount, recipe_ingredient_measurement) = read_recipe_information(recipe_name = recipe)
                print(("recipe serving size = %(size)i") % {"size":recipe_serving_size})
            # if the count for each recipe is different from the serving size
                if servings_needed != recipe_serving_size:
                    serving_size_difference = (servings_needed / recipe_serving_size)
                    # unpack tuple and convert amount of ingredients to be correct amount
                    recipe_ingredient_amount = load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference)
                else:
                    recipe_ingredient_amount = unpack_ingredient_amount(*recipe_ingredient_amount)
        # add ingredients to grocery list
                recipe_ingredient_names = unpack_ingredient_names(*recipe_ingredient_names)
                recipe_ingredient_measurement = unpack_ingredient_measurement(*recipe_ingredient_measurement)
                ingredient_names = add_ingredient_info_to_list(
                        ingredient_info = recipe_ingredient_names,
                        info_list = ingredient_names)
                ingredient_amounts = add_ingredient_info_to_list(
                        ingredient_info = recipe_ingredient_amount,
                        info_list = ingredient_amounts)
                ingredient_measurements = add_ingredient_info_to_list(
                        ingredient_info = recipe_ingredient_measurement,
                        info_list = ingredient_measurements)
                
                check_for_ingredient(ingredient_names, final_ingredient_names,
                         ingredient_amounts, final_ingredient_amounts,
                         ingredient_measurements, final_ingredient_measurements)
                print(final_ingredient_names)
                print(final_ingredient_amounts)
                print(final_ingredient_measurements)
        
        # output final grocery list

# unpacks items in recipe_ingredient_amount and returns them as a list of ints

def unpack_ingredient_amount(recipe_ingredient_amount):
    recipe_ingredient_amount = [int(amount) for amount in recipe_ingredient_amount.split(",")]
    return recipe_ingredient_amount        
        
# converts amounts to the correct amount needed based on serving_size_difference
        
def load_correct_amount_of_ingredients(recipe_ingredient_amount, serving_size_difference):
    recipe_ingredient_amount = unpack_ingredient_amount(*recipe_ingredient_amount)
    recipe_ingredient_amount[:] = [(amount * serving_size_difference) for amount in recipe_ingredient_amount]
    return recipe_ingredient_amount   

def unpack_ingredient_names(recipe_ingredient_names):
    recipe_ingredient_names = [str(name) for name in recipe_ingredient_names.split(",")]
    return recipe_ingredient_names

def unpack_ingredient_measurement(recipe_ingredient_measurement):
    recipe_ingredient_measurement = [str(measurement) for measurement in recipe_ingredient_measurement.split(",")]
    return recipe_ingredient_measurement

def add_ingredient_info_to_list(ingredient_info, info_list):
    for info in ingredient_info:
        info_list.append(info)
    return info_list

def check_for_ingredient(ingredient_names, final_ingredient_names,
                         ingredient_amounts, final_ingredient_amounts,
                         ingredient_measurements, final_ingredient_measurements):
    for ingredient in ingredient_names:
        ingredient_index = ingredient_names.index(ingredient)
        if ingredient not in final_ingredient_names:
            final_ingredient_names.append(ingredient)
            final_ingredient_amounts.append(ingredient_amounts[ingredient_index])
            final_ingredient_measurements.append(ingredient_measurements[ingredient_index])
        elif ingredient in final_ingredient_names:
            final_index = final_ingredient_names.index(ingredient)
            # do this at the correct index corresponding to the name
            if ingredient_measurements[ingredient_index] == final_ingredient_measurements[final_index]:
                final_ingredient_amounts[final_index] = final_ingredient_amounts[final_index]+(ingredient_amounts[ingredient_index])
            # elif ingredient_measurement[ingredient_index] != final_ingredient_measurement[final_index]:
                # convert the two amounts to be in the same measurement
                # add amounts together
                # convert to largest conversion available in whole numbers

# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:38:12 2018

@author: MANHARDTD
"""

def food_list_creation():
    # main menu asks user if they want to enter a recipe, create a food list, or exit
    main_menu()
    # go through recipes after they are picked and add their ingredients to a shopping_list that will be output
    # as a text (?) file    
    # exit loop and program
    
    

#Main menu takes user input and checks against the different choices allowed

def main_menu():
    while True:
        main_menu_choice = input('What would you like to do? \n\
1)Enter a recipe \n\
2)Create a food list \n\
3)Exit \n\
Your input: ')
        #choice 1 would run the EnterNewRecipe function
        if main_menu_choice == "1":
            recipe_df = read_recipe_storage()
            enter_new_recipe(recipe_df)
        elif main_menu_choice == "2":
            recipe_df = read_recipe_storage()
            final_recipe_dataframe = recipe_selection(recipe_df)
            grocery_df = create_grocery_list(recipe_df, final_recipe_dataframe)
            output_grocery_list(grocery_df)
            break
        elif main_menu_choice == "3":
            quit()
            break
        else:
            print("That was not a valid option, \
please enter an integer (1-3) for your choice")
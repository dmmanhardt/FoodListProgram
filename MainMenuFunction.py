# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:55:15 2018

@author: MANHARDTD
"""

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
            enter_new_recipe()
        elif main_menu_choice == "2":
            recipe_selection()
        elif main_menu_choice == "3":
            quit()
            break
        else:
            print("That was not a valid option, \
please enter an integer (1-3) for your choice")
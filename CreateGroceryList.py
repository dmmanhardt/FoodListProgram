# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:23:34 2018

@author: David
"""

# takes final dataframe with recipes for each meal, and reads each recipes ingredients, outputs grocery list as text file with
# today's date in name

def create_grocery_list(df):
    print("called create_grocery_list")
    for recipe in df["Breakfast"]:
        print(recipe)
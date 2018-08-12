# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:53:30 2018

@author: David
"""

# once recipes for each meal/day are selected, grab the ingredients from the recipe_list
# and add them to a text file (?)

# Create a dataframe to store recipes in?
# recipe_name    serving_size    ingredient 1  ingredient 2

#need to concentrate on HOW to store the recipes, adding/deleting can be figure out after

# step 1: figure out how to associate the attributes with each recipe
# step 2: figure out how to store them to a list and read them correctly
# step 3: figure out how to do that for multipe recipes and save them

# IDEAS:

# read all recipes in pickle file, then dump them to their own variables, create classes for each, and store those variables in a list
# if there are new recipes, add those recipes to the list
# add all recipes from list back to pickle file

# one text file with all recipe names, each recipe name has it's own text file with list of ingredients?

# database with one column recipe names, next column list of ingredients, next column list of amounts for those ingredients (would both be
# at the same index), etc
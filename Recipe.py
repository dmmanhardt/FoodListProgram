# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:48:15 2018

@author: MANHARDTD
"""

class Recipe:
    
    def __init__(self):
        self.recipe = set()
        
    def check(self, recipe):
        return recipe.lower() in self.recipe
    
    def load(self, RecipeList):
        file = open(recipe, "r")
        for line in file:
            self.recipe.add(line.rstrip("\n"))
        file.close()
        return True
    
    def size(self):
        return len(self.recipe)
    
    def unload(self):
        return True
    
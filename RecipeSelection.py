# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:20:32 2018

@author: David
"""
import pandas as pd

def recipe_selection(days_for_meal_prep, days_for_breakfast, days_for_lunch, days_for_dinner):
    print("We will now select recipes for ", days_for_meal_prep)
    df = pd.DataFrame(columns = days_for_meal_prep)
    print(df)
    return df
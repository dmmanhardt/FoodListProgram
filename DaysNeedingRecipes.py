# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:40 2018

@author: MANHARDTD
"""
def DaysNeedingRecipes():
    ValidNumberOfDays = False
    while ValidNumberOfDays == False:
        NumberOfDaysToPlanFor == input("Type the number of days you want to make a list for: ")
        #create array with # of nights as key
            if 1 < NumberOfDaysToPlanFor < 7:
                NumberOfDays(NumberOfDaysToPlanFor)
            else:
                print("That is not a valid input, please enter an integer.")
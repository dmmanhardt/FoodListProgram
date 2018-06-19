# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:40 2018

@author: MANHARDTD
"""

#takes user input for the amount of days to plan recipes for, and creates a list with that number of days
#or creates a variable for each day with breakfast, lunch, and dinner?
def DaysNeedingRecipes():
    ValidNumberOfDays = False
    while ValidNumberOfDays == False:
        #takes user input as int to compare against the number of valid days
        #change to check if NumberOFDaysToPlan for is a number, not string, then convert to int and compare to 0 < x < 8
        NumberOfDaysToPlanFor = int(input("Type the number of days you want to make a list for as an integer: "))
        #checks to see if the number of days is between 1-7
        if 0 < NumberOfDaysToPlanFor < 8:
            ValidDaySelected = False
            #FIX LIST 
            ValidDays = (sunday, monday, tuesday, wednesday, thursday, friday, saturday)
            while ValidDaySelected == False:
                #takes user input and converts to lowercase in order to compare to valid days of the week
                DayToStartOn = input("What day will the list start on? ").lower()
                if DayToStartOn not in ValidDays:
                    print("That is not a valid day")
                else:
                    ValidDaySelected = True
                    NumberOfDays(NumberOfDaysToPlanFor, DayToStartOn)
        else:
            print("That is not a valid input, please enter an integer.")

#take user input of how many days to plan for and makes arrays to store the info                
#def NumberOfDays(NumberOfDaysToPlanFor):
    
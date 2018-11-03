def days_to_plan_for(start_day, number_days):
    valid_days = ("Sunday", "Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday")
    index = valid_days.index(start_day)
    # doubling the list since before the script would not be able to 
    # loop over the list more than twice
    valid_days = valid_days * 2
    days_for_meal_prep = []
    days_for_meal_prep = (valid_days + valid_days)[index:index + number_days]
    return days_for_meal_prep
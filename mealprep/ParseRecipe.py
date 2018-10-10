
def parse_ingredient_info(ingredient_info):
    amounts = []
    measurements = []
    ingredients = []
    measurement_units = ['lb', 'cup', 'tbsp']
    ingredient_info = format_ingredient_info(ingredient_info)
    for row in ingredient_info:
        amount = None
        measurement = None
        ingredient = None
        removal_list = []
        row = row.split()
        for word in row:
            # if int in word or if word is fraction or decimal
            if check_for_numbers(word) == True:
                amount = word
            elif word in measurement_units:
                measurement = word
                removal_list.append(measurement)
            else:
                continue
        # remove amount and measurement from row, name is rest of row
        ingredient = [word for word in row if word not in removal_list]
        ingredient = ' '.join(ingredient)
        if amount is not None:
            amounts.append(amount)
        if measurement is not None:
            measurements.append(measurement)
        if ingredient is not None:
            ingredients.append(ingredient)
    print(amounts)
    print(measurements)
    print(ingredients)

    # zip together lists
    #return zipped list
    
def format_ingredient_info(ingredient_info):
    ingredient_info = [info.strip() for info in ingredient_info.split('\n')]
    return ingredient_info

def check_for_numbers(word):
    return (any(position.isdigit() for position in word))
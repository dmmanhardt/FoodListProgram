from fractions import Fraction

def parse_ingredient_info(ingredient_info):
    amounts = []
    measurements = []
    ingredients = []
    measurement_units = {"cup": ["cups", "cup", "c.", "c"], "fluid_ounce": ["fl. oz.", "fl oz", "fluid ounce", "fluid ounces"],
         "gallon": ["gal", "gal.", "gallon", "gallons"], "ounce": ["oz", "oz.", "ounce", "ounces"],
         "pint": ["pt", "pt.", "pint", "pints"], "pound": ["lb", "lb.", "pound", "pounds"],
         "quart": ["qt", "qt.", "qts", "qts.", "quart", "quarts"],
         "tablespoon": ["tbsp.", "tbsp", "T", "T.", "tablespoon", "tablespoons", "tbs.", "tbs"],
         "teaspoon": ["tsp.", "tsp", "t", "t.", "teaspoon", "teaspoons"],
         "gram": ["g", "g.", "gr", "gr.", "gram", "grams"], "kilogram": ["kg", "kg.", "kilogram", "kilograms"],
         "liter": ["l", "l.", "liter", "liters"], "milligram": ["mg", "mg.", "milligram", "milligrams"],
         "milliliter": ["ml", "ml.", "milliliter", "milliliters"], "pinch": ["pinch", "pinches"],
         "dash": ["dash", "dashes"], "touch": ["touch", "touches"], "handful": ["handful", "handfuls"],
         "stick": ["stick", "sticks"], "clove": ["cloves", "clove"], "can": ["cans", "can"], "large": ["large"],
         "small": ["small"], "scoop": ["scoop", "scoops"], "filets": ["filet", "filets"], "sprig": ["sprigs", "sprig"]}
    ingredient_info = format_ingredient_info(ingredient_info)
    for row in ingredient_info:
        amount = ''
        measurement = ''
        ingredient = ''
        removal_list = []
        row = row.split()
        for word in row:
            if check_for_numbers(word) == True:
                removal_list.append(word)
                word = float(sum(Fraction(s) for s in word.split()))
                if amount != '':
                    amount += word
                else:
                    amount = word
            elif any(word in unit for unit in measurement_units.values()) == True:
                measurement = word
            else:
                continue
        removal_list.append(measurement)
        # remove amount and measurement from row, ingredient is rest of row
        ingredient = [word for word in row if word not in removal_list]
        ingredient = ' '.join(ingredient)
        if amount is not None:
            amounts.append(amount)
        if measurement is not None:
            measurements.append(measurement)
        if ingredient is not None:
            ingredients.append(ingredient)
    recipe_info = Recipe(amounts, measurements, ingredients)
    return recipe_info

    
def format_ingredient_info(ingredient_info):
    ingredient_info = [info.strip() for info in ingredient_info.split('\n')]
    #remove blank rows from ingredient_info
    ingredient_info = list(filter(None, ingredient_info))
    return ingredient_info

def check_for_numbers(word):
    return (any(position.isdigit() for position in word))

#create Recipe class and add amounts, measurements, and ingredients as attributes
# in order to return single class object
class Recipe:
    def __init__(self, amounts, measurements, ingredients):
        self.amounts = amounts
        self.measurements = measurements
        self.ingredients = ingredients
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

#dictionary mappping  iis when we replace dictionaries with switch statements
def get_names(foods):
    names = []
    
    for food in foods:
        names.append(food['name']) 
    return names
def get_spiciest_foods(spicy_foods):
     return [food for food in spicy_foods if food['heat_level'] > 5 ]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return dict(food)

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: { '🌶' * food['heat_level']}")

    
def get_average_heat_level(spicy_foods):
    ##its static not dynamic
    return sum([food['heat_level'] for food in spicy_foods]) / len(spicy_foods)    #if no foods return 0

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
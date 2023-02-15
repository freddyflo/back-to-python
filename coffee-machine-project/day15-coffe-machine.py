MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#### money  #####
# quarter = 0.25
# dime = 0.10
# nickel = 0.05
# penny = 0.01

def user_money(user_quarter, user_dimes, user_nickels, user_penny):
    return float((user_quarter + user_dimes + user_nickels + user_penny))


def get_cafe_price(cafe_type):
    return MENU[cafe_type]['cost']

def get_cafe_water(cafe_type):
    return MENU[cafe_type]['ingredients']['water']

def get_cafe_milk(cafe_type):
    return MENU[cafe_type]['ingredients']['milk']

def get_cafe_level(cafe_type):
    return MENU[cafe_type]['ingredients']['coffee']

def get_resource_water():
    return resources['water']

def get_resource_coffee():
    return resources['coffee']

def get_resource_milk():
    return resources['milk']

def update_resource_info(water, milk, coffee):
    resources['water'] -= water 
    resources['coffee'] -= coffee 
    resources['milk'] -= milk 

def update_resource_info_espresso(water, coffee):
    resources['water'] -= water 
    resources['coffee'] -= coffee 
    

def add_money_machine(total, coffee_price):
    total += coffee_price
    return total


def user_change(user_coins, coffee_type):
    return float(user_coins - get_cafe_price(coffee_type))

def get_report():
    print(f"Water: {get_resource_water()}ml")
    print(f"Milk: {get_resource_milk()}ml")
    print(f"Coffee: {get_resource_coffee()}g")
    #print(f"Money: ${get_machine_money()}")

def update_cafe_info(cafe_type, water, coffee, milk):
    MENU[cafe_type]['ingredients']['water'] = water
    MENU[cafe_type]['ingredients']['coffee'] = coffee
    if cafe_type == "latte" or cafe_type == "cappuccino":
        MENU[cafe_type]['ingredients']['milk'] = milk
    print(f"{MENU}")


def can_buy_coffee(user_money, coffee_price):
    if user_money > get_cafe_price(coffee_price):
        return True
    else:
        return False

def compare_resources(coffee_type):
    if coffee_type == "latte" or coffee_type == "cappuccino":
        if get_cafe_milk(coffee_type) > get_resource_milk():
           print(f"Insufficient milk")
           return False
    if get_cafe_water(coffee_type) > get_resource_water():
        print(f"Insufficient water")
        return False
    elif get_cafe_level(coffee_type) > get_resource_coffee():
        print(f"Insufficient coffee")
        return False
    else:
        return True
    





def start():

    # refactor to a add loop
    money_in_machine = 0
    user_request = input(f"What would you like ? (espresso/latte/cappuccino/report): ")
    if user_request == "report":
        get_report()
    elif user_request == "espresso" or  user_request == "latte" or  user_request == "cappuccino":
        enough_resources = compare_resources(user_request)
        if enough_resources:
            print(f"Please insert coins.")
            quarters = float(input(f"How many quarters?: "))
            dimes = float(input(f"How many dimes?: "))
            nickels = float(input(f"How many nickels?: "))
            penny = float(input(f"How many penny?: "))
            money = user_money(quarters,dimes,nickels,penny)
            buy_coffee = can_buy_coffee(money,user_request)
            if buy_coffee:
                change = user_change(money,user_request)
                print(f"Here is ${change} in change")
                print(f"Here is your {user_request}. Enjoy!")
                if user_request == "espresso":
                    update_resource_info_espresso(get_cafe_water(user_request), get_cafe_level(user_request))
                else:
                    update_resource_info(get_cafe_water(user_request), get_cafe_milk(user_request), get_cafe_level(user_request))
                money_in_machine = add_money_machine(money_in_machine, get_cafe_price(user_request))
                get_report()
            else:
                print("******* Not enough money ********")
        else:
            print("Insufficient resource")

start()
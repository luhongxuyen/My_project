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

coin = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def coin_calculate() -> float:
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * coin["quarter"]
    dimes = int(input("How many dimes?: ")) * coin["dime"]
    nickels = int(input("How many nickels?: ")) * coin["nickel"]
    pennies = int(input("How many pennies?: ")) * coin["penny"]

    total = quarters + dimes + nickels + pennies

    return total


def check_resources_sufficient(available_water: int, available_milk: int, available_coffee: int, current_coffee: dict):
    water_cost = current_coffee["water"]
    coffee_cost = current_coffee["coffee"]
    if "milk" in current_coffee:
        milk_cost = current_coffee["milk"]
    else:
        milk_cost = 0

    if available_water < water_cost:
        return f"Sorry there is not enough water."
    elif available_milk < milk_cost:
        return f"Sorry there is not enough milk."
    elif available_coffee < coffee_cost:
        return f"Sorry there is not enough coffee."
    else:
        global water, milk, coffee
        water = available_water - water_cost
        milk = available_milk - milk_cost
        coffee = available_coffee - coffee_cost


on_mode = True
emoji = "☕"
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
change = 0


while on_mode:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

    elif user_input == "off":
        print("Good bye...")
        on_mode = False

    elif user_input in MENU:
        coffee_type = MENU[user_input]
        coffee_ingredients = coffee_type["ingredients"]

        if isinstance(check_resources_sufficient(water, milk, coffee, coffee_ingredients), str):
            print(check_resources_sufficient(water, milk, coffee, coffee_ingredients))
        else:
            total_insert_coin = coin_calculate()

            if total_insert_coin < coffee_type["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += coffee_type["cost"]
                change = round(total_insert_coin - coffee_type["cost"], 2)
                print(f"Here is ${change} in change.\nHere is your {user_input} {emoji} Enjoy!")

    else:
        print(f"Sorry, we don't have '{user_input}' coffee.")

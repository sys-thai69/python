

machine_off = False
money = 0.0

ingredients_list = {
    "water": 2000,
    "milk": 1000,
    "coffee": 500,
}

Menu = {
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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}

def check_resources(order_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in order_ingredients:
    if order_ingredients[item] > ingredients_list[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

while not machine_off:
  user_buying = False
  while not user_buying:
    print("Welcome to the coffee machine!")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
      print(f"Water: {ingredients_list['water']}ml")
      print(f"Milk: {ingredients_list['milk']}ml")
      print(f"Coffee: {ingredients_list['coffee']}g")
      print(f"Money: ${money}")
    elif user_choice == "off":
      machine_off = True
      user_buying = True
    else:
      drink = Menu[user_choice]
      if check_resources(drink["ingredients"]):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total_inserted = quarters + dimes + nickels + pennies
        if total_inserted < drink["cost"]:
          print("Sorry that's not enough money. Money refunded.")
          user_buying = True
        else:
          change = round(total_inserted - drink["cost"], 2)
          if change > 0:
            print(f"Here is ${change} in change.")
          money += drink["cost"]
          for item in drink["ingredients"]:
            ingredients_list[item] -= drink["ingredients"][item]
          print(f"Here is your {user_choice} ☕️. Enjoy!")
          user_buying = True

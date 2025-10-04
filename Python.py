def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"Its name is {pet_name.title()}.")

# Using keyword arguments (order doesn't matter)
describe_pet(pet_name='Buddy', animal_type='dog')

def make_shirt(size='large', message='I love Python'):
    print(f"Making a {size} shirt with the message: '{message}'.")

# Uses default size and message
make_shirt()
# Overrides only the message
make_shirt(message='Code with passion')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni', 'mushrooms', 'extra cheese')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# Output: {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}

y = 20 # y is global

def modify_global():
    global y
    y = 30 # This modifies the global y

print(y) # Output: 20
modify_global()
print(y) # Output: 30
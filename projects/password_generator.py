import random

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_letters = lowercase_letters + uppercase_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

number_of_letters = int(input("how many letters would you like in your password?\n"))
number_of_symbols = int(input("how many symbols would you like?\n"))
number_of_numbers = int(input("how many numbers would you like?\n"))

password_list = []
for i in range(0, number_of_letters):
  password_list.append(random.choice(all_letters))

for i in range(0, number_of_symbols):
  password_list.append(random.choice(symbols))

for i in range(0, number_of_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
  password += char

print (f"Your random password is: {password}")
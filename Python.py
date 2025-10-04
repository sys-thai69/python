import random


random_num = random.randint(1,100)

list_num = []

for i in range(10):
  list_num.append(random.randint(1,100))

print(list_num)

highest_num = 0
for num in list_num:
  if num > highest_num:
    highest_num = num

print("The highest number is:", highest_num)

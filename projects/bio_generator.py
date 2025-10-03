print("we are trying to get some information from bio generator")

bio_name = input("enter your name: ")
bio_age = int(input("enter your age: "))
bio_gender = input("enter your gender: ")
bio_country = input("enter your country: ")

from datetime import date
current_year = date.today().year
birthyear = current_year - bio_age


print(f"hello {bio_name}!")
print(f"you are a {bio_gender} currently {bio_age} years old")
print(f"you were born in the year {birthyear}")

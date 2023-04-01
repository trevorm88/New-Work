#RANDOM NAME GENERATOR

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

ran_number = len(names)
ran_choice = random.randint(0, ran_number - 1)
name_chosen = names[ran_choice]
print(name_chosen + " is going to buy the meal today!")

''' 
name_chosen = random.choice(names)
print(name_chosen)
'''



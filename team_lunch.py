# Split string method
import random
names_string = input("Who is going to buy team lunch?\n\nGive me everybody's names, separated by a comma. and I will pick one ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

loser = random.choice(names)

print(loser + " is going to buy the meal today!")
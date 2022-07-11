# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine = name1.lower() + name2.lower()
t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")

true = t+r+u+e 

l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e") 

love = l+o+v+e

love_score = int(str(true)+str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
#this program calculates whethe any given year is leap year or not

year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 != 0:
    print("Not leap year")
else:
    print("Leap year")
print("Wecome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip/100 * bill + bill
each_person = (bill_with_tip / people)
final = "{:.2f}".format(each_person)
#print(150.00 / 5) * 1.12 = 33.6)

print(f"Each person should pay: {final}")
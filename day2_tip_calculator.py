print("Welcome to the tip calculator!!")

bill = float(input("Please enter the total bill $"))
tip = int(input("How much you would like to tip eg. 10, 15, 22, 20 "))
people = int(input("How many people to split the bill "))

#Calculate the bill plus the tip
bill_plus_tip = tip/100 * bill + bill

#Calculate bill plus tip for each person
bill_per_person = bill_plus_tip / people

#format the total for each person
final_bill = "{:.2f}".format(bill_per_person)

#print the formated total on the screen
print(f"Total bill for each person is ${final_bill}")


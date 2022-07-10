age = int(input("What is your current age? "))

#define the age number to be used
years_remaining = 90 - age

#calculate months, weeks and days
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks and {days_remaining} days left\n Note: this assumes"

print(message)
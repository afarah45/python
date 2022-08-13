# def greet(name):
#     print(f"Hello Mr.{name}! Welcome to our resort.")
#
#
# guests = input("what is your name? ")
#
# greet(guests)

class User:
    pass


user_1 = User()
user_1.username = "farah"
print(user_1.username)


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles = 0

    def miles(self):
        self.miles += 1


kia = Car("Kia", "Telluride", 2020, "white")
audi = Car("Audi", "A4 Quattro", 2011, "white")
print(f"Car details: {kia.make} {kia.model} {kia.year} {kia.color}")
audi.miles = 20
print(audi.miles)

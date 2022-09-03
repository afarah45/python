class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
#to inherit the animal class add the upser keyword and initialize it
class Fish(Animal):
    def __init__(self):
        super().__init__()
#to inherit specific functuion add more to it. use the super keyword followed by function name,then add 
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()

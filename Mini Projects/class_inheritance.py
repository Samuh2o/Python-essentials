class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# the call to super() in the initialiser is recommended, but not strictly required..
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "friendly"

rex = Labrador()

print(rex.temperament)
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
            print("I am moving in water")



nemo = Fish()
nemo.swim()
nemo.breathe()
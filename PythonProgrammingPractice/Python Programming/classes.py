class abc:
    def __init__(self, car, bike):
        self.car = car
        self.bike = bike
    
    def methodone(self):
        print(f"Car is {self.car}")
        print(f"Bike is {self.bike}")

objectone = abc("ford", "bikeone")
objectone.methodone()
class car:
    def __init__(self ,brand,model):
        self.brand = brand
        self.model = model
    def display_info(self):
        return f"car:{self.brand} {self.model}"
car = car("Toyota","corolla")
print(car.display_info())
        




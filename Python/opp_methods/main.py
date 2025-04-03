    #1: Instance method

# class car:
#     def __init__(self ,brand,model):
#         self.brand = brand
#         self.model = model
#         """ instance method"""
#     def display_info(self):
#         return f"car:{self.brand} {self.model}"
# car = car("Toyota","corolla")
# print(car.display_info())
        
        #2: Class method

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        """class method"""
    @classmethod
    def display_info(cls):
        return f"car:{cls.brand} {cls.model}"
car.brand = "Audi"
car.model = "RS8"
print(car.display_info()) 
        






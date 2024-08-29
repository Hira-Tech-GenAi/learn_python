class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !" 

    def full_name(self):# method
        return f"{self.__brand} {self.__model}" # formatted string 

    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "This is awesome car"
    @property
    def model(self):
        return self.__model




#inherit class
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("tesla", "Model S", "85kwh")
print(isinstance("tesla", Car))
print(isinstance("tesla", ElectricCar))

my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")
print(Car.general_description())
print(my_car.general_description())



"""my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

your_car = Car("Tata", "Safari")
print(your_car.brand)"""
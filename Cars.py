from abc import ABC, abstractmethod

class AbstractClass(ABC):                # Abstrakcja
    def __init__(self, brand, model):
        self._brand = brand              # Enkapsulacja
        self._model = model
    
    @abstractmethod
    def drive():
        pass
    
class NewClass(AbstractClass):
    pass

class Car:      # Klasa
    def __init__(self, brand, model):
        self._brand = brand              # Enkapsulacja
        self._model = model

    def drive(self):
        return self._brand + ' ' + self._model + ' drives'

class Vehicle(Car):                       # Dziedziczenie
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self._fuel_type = fuel_type
    
    def get_fuel_type(self):
        return self._fuel_type
    
    def drive(self):
        return self._brand + ' ' + self._model + ' drives on ' + self._fuel_type

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, fuel_type="electric")
        self._battery_capacity = battery_capacity

    def drive(self):
        return self._brand + ' ' + self._model + ' drives on, ' + self._battery_capacity + ' kWh'


my_car = Car('Toyota', 'Corolla')       # Obiekt klasy
print(my_car.drive())                   # Wywołanie metody

my_car1 = Car('Volvo', 'XC60')
print(my_car1.drive())

my_car2 = Vehicle('Toyota', 'Corolla', 'Electric')
print(my_car2.drive())

my_car4 = ElectricCar('Tesla', 'Model S', '97')
print(my_car4.drive())

# my_car5 = Car('A', 'B', 'C')
# self - też jest argumentem, tyle że jest niewidoczny
# takes 3 positional arguments but 4 were given





# Enksapsulacja
# Dziedziczenie
# Polimorfizm
# Abstrakcja


# my_car_brand 
# my_car_model
# my_car_color 
#print(my_car + my_model + 'drives')
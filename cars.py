class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def _drive(self):
        return self.brand + ' ' + self.model + ' drives'
    
    my_car = Car('Opel', 'Astra')
    print(my_car.drive())
    

#this is a class that describes cars
#class classname :
class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,colour,horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.horse_power= horse_power
    def print_make(self,make):
        print("The make of  the car is an {0} ".format(self.make))
    def set_make(self,make):
        self.make = make
    def get_make(self):
        return self.make
    def set_colour(self,colour):
        self.colour = colour
    def get_colour(self):
        return self.colour







my_car = car("Subaru","Imprezza","2010","2800cc","grey","500hp")

friends_car = car("Note","Nissaan","2010","1400cc","green","200hp")
my_car.print_make("Imprezza")
my_car.set_make("Ford")
friends_car.set_make("Isuzu")
print(my_car.get_make())
print(friends_car.get_make())


my_car.set_colour("Black")
friends_car.set_colour("Purple")
print(my_car.get_colour())
print(friends_car.get_colour())




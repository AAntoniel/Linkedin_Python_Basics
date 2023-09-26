#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
   # Method that get called when the class get constructed and initialized __init__
   # __init__ is the function Python calls when the object has been created and its time to initialize the object's data
   def __init__(self, bodystyle):
      # It's defined a property on the class and it's going to hold the value that was passed in to the class when it's created
      self.bodystyle = bodystyle
      # Other classes can be created that derives from this class

   def drive(self, speed):
      self.mode = "driving"
      self.speed = speed

   def model(self, model1):
      self.model1 = model1
    
class Car(Vehicle):
   def __init__(self, enginetype):
      # The 'superclass' must be initialized, the vehicle class, by using the 'superfunction'
      # It's also called as father class
      super().__init__("Car") 

      # Other properties can be specified to the 'Car' class
      self.wheels = 4
      self.doors = 4
      self.enginetype = enginetype 
    
   def drive(self, speed):
      super().drive(speed)
      print("Driving my", self.enginetype, "car at", self.speed)

   def model(self, model1):
      super().model(model1)
      print("Driving my", self.enginetype, self.model1)

class Motorcycle(Vehicle):
   def __init__(self, enginetype, hassidecar):
      super().__init__("Mototcycle")
      if (hassidecar):
         self.wheels = 3
      else:
         self.wheels = 2

      self.doors = 0
      self.enginetype = enginetype

   def drive(self, speed):
      super().drive(speed)
      print("Driving my", self.enginetype, "motorcycle at", self.speed)
    
   def model(self, model1):
      super().model(model1)
      print("Driving my", self.enginetype, self.model1)

# With the classes defined, create specific objects of those types
# It's used the name of the class along with the parameters for the init function

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
mc2 = Motorcycle("electric", False)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.model('Mustang')
car2.drive(40)
mc1.drive(50)
mc2.model("Harley")
class car:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

    def move(self):
      print("Drive!")

class boat: 
  def _init_(self, brand, model):
    self.brand = brand 
    self.model = model

    def move(self):
      print("sail!")

class plane:
  def _init_(self, brand, model):
    self.brand = brand
    self.model = model

    def move(self):
      print("fly!")
car1 = car("ford", "mustang")       #create a car class
boat1 = boat("Ibiza", "Touring 20") #create a boat class
plane1 = plane("boeing", "747")     #create a plane class

for x in (car1, boat1, plane1):
  x.move()
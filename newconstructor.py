class Car:
    def __init__(self, year,  maker, make, model, engine, doors, color, roof):
        self.year = year
        self.make = make
        self.maker = maker
        self.model = model
        self.engine = engine
        self.doors = doors
        self.color = color
        self.roof = roof

    def say_car(self):
        return "This is  a {} {} {} {} {} {} {} {}".format(self.year,
                                                           self.make,
                                                           self.maker,
                                                           self.model,
                                                           self.engine,
                                                           self.doors,
                                                           self.color,
                                                           self.roof)


dreamcar = Car("1969", "Chevrolet", "Chevelle",
               "SS", "396", "2", "Creame", "Convertible")
bobscar = Car("1972", "Ford", "Mustang", "Elinor",
              "KR", "2", "Teal", "Convertible")
print(dreamcar.say_car())
print(bobscar.say_car())

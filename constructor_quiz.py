class Person:
    # creates a class with prepopulated characteristicis
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "hi, my names is {}".format(self.name)


some_person = Person("bob")
print(some_person.greeting())

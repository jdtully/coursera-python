class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name
        self.category = ""

    def set_category(self, category):
        self.category = category


Turtle = Animal("fred")
Turtle.category = "reptile"

Snake = Animal("suzy")
Snake.category = "reptile"

print(Turtle.category)
print("Snakes  are  " + Snake.category+"'s")


class Zoo:
    def __init__(self):
        self.current_animals = {}
        self.count = 0

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal.category == category:
                result += 1
        return result


zoo = Zoo()

turtle = Turtle("Turtle")
Turtle.category = "reptile"
snake = Snake("Snake")

zoo.add_animal(turtle)
zoo.add_animal(snake)

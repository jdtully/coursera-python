class Piglet:
    years = 0

    def pig_years(self):
        return self.years * 18

    def speak(self):
        print("Oink! I'm {} I am {} years old! Oink".format(self.name, self.years))


hamlet = Piglet()
hamlet.name = "Hamlett"

hamlet.years = 2
hamlet.pig_years()
hamlet.speak()
petunia = Piglet()
petunia.name = "Petunia"

petunia.years = 3
petunia.pig_years()
petunia.speak()

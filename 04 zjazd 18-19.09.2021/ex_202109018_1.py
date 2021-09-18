class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Animal is speaking')


class Mammal(Animal):
    def drink_milk(self):
        print('Drinking milk')



mammal = Mammal('Tiger')
print(mammal)
mammal.speak()
mammal.drink_milk()

# class Bike:
#     def __init__(self, color):
#         self.wheels = 4
#         self.color = color


# animal1 = Animal("Dragon")
# animal2 = Animal("Tiger")
# # animal3 = Animal("Lion")
# print(animal1.name)
# print(animal2.name)
# animal1.speak()
# animal2.speak()
# print(animal3.name)

# bike1 = Bike(color='blue')
# print(bike1.color)
# print(bike1.wheels)

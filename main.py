import time


class Animals:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


class Cars:
    def __init__(self, name, brand, weight):
        self.name = name
        self.brand = brand
        self.weight = weight


cl1st1 = Animals(name='Tiger', age=4, weight=209.8)
cl1st2 = Animals(name='Cat', age=6, weight=1.4)
cl1st3 = Animals(name='Dog', age=5, weight=23.2)


print("Animals(class1)")
print(" ")


time.sleep(3)


print("Name:", cl1st1.name, "age:", cl1st1.age, "weight:", cl1st1.weight)
print("Name:", cl1st2.name, "age:", cl1st2.age, "weight:", cl1st2.weight)
print("Name:", cl1st3.name, "age:", cl1st3.age, "weight:", cl1st3.weight)




time.sleep(5)


cl2st1 = Cars(name='Vesta', brand="LADA", weight="1230 kg")
cl2st2 = Cars(name='EQE SUV', brand="Mercedes-Benz", weight="1800 kg")
cl2st3 = Cars(name='X1', brand="BMW", weight="1930 kg")


print(" ")
print("cars(class2)")
print(" ")


time.sleep(2)


print("Name:", cl2st1.name, "brand:", cl2st1.brand, "weight:", cl2st1.weight)
print("Name:", cl2st2.name, "brand:", cl2st2.brand, "weight:", cl2st2.weight)
print("Name:", cl2st3.name, "brand:", cl2st3.brand, "weight:", cl2st3.weight)


time.sleep(3)
class Person:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def __str__(self):
        return f"სახელი: {self.first_name} გვარი: {self.last_name} ასაკი: {self.age} სიმაღლე: {self.height}"

p1 = Person("ზურა", "ილურიძე", 12, 1.57)
print(p1)

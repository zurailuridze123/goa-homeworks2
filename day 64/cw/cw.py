# 1)  შევქმანთ class რომელსაც დავაქმევთ Person და შევქმნით lower() ფუნქცია
class Person:
    def __init__(self, name):
        self.name = name

    def lower_name(self):
        return self.name.lower()
person1 = Person("zura")
lower_name = person1.lower_name()
print(lower_name) 

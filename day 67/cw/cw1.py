class Person:
    def __init__(self, name, surname, fathers_name):
        self.name = name
        self.surname = surname
        self.fathers_name = fathers_name

    def __str__(self): 
        return f"Name: {self.name}, Surname: {self.surname}, Father's Name: {self.fathers_name}"

# Example usage:
zura = Person("ზურა", "ილურიძე", "მიშო")
print(zura)
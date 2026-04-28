# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("{} {}".format(self.name, self.age))

# Child class
class Student(Person):
    def __init__(self, name, age, dob):
        # Call the constructor of the Person class
        super().__init__(name, age)
        self.dob = dob

    def displayInfo(self):
        print("{} {} {}".format(self.name, self.age, self.dob))

# Create an object of the Student class
obj = Student("Rahul", 23, "16-03-2000")

# Call methods to display information
obj.display()        # Output: Rahul 23
obj.displayInfo()    # Output: Rahul 23 16-03-2000

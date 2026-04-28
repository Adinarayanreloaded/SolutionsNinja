from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

# Instantiate objects of each concrete class
human = Human()
snake = Snake()
dog = Dog()
lion = Lion()

# Call the move method on each object
human.move()
snake.move()
dog.move()
lion.move()

# -------------- P1 --------------
class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} & Marks: {self.marks}")

obj1 = Student("Muhammad Omer", 40)
obj1.display()

# -------------- P2 --------------
class Counter:
    count = 0

    def __init__(self) -> None:
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_count()

# -------------- P3 --------------
class Car:
     def __init__(self, brand):
        self.brand = brand

     def start(self):
        print(f"{self.brand} car has started.")

my_car = Car("BMW")

print(f"Car Brand: {my_car.brand}")

my_car.start()

# -------------- P4 --------------
class Bank:
    bank_name = ""

    def change_bank_name(cls, name):
        bank_name = name
        print(f"Bank Name has been changed to: {name}")

bank_obj = Bank()
bank_obj.bank_name = "HBL"

bank_obj.change_bank_name("Bank Alfalah")

# -------------- P5 --------------
class MathUtils:
    @staticmethod
    def add (a, b):
        return a + b 
    
result = MathUtils.add(5,9)
print(result)

# -------------- P6 --------------
class Logger:
    def __init__(self):
        print("Logger initialized. Object created.")

    def __del__(self):
        print("Logger destroyed. Object deleted.")

log = Logger()

del log

# -------------- P7 --------------
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name   
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Muhammad Omer", 500000, "123-45-6789")

# Access public variable
print(f"Public: {emp.name}")  # ✅ Accessible

# Access protected variable
print(f"Protected: {emp._salary}")  # ⚠️ Accessible, but not recommended

# Access private variable
try:
    print(f"Private: {emp.__ssn}")  # ❌ Will raise AttributeError
except AttributeError as err:
    print(f"Private: Cannot access directly: {err}")

# -------------- P8 --------------
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")

teacher_obj = Teacher("Sir Asharib", "Python")

# -------------- P9 --------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area of Rectangle: {rect.area()}")

# -------------- P10 --------------
class Dog:
    def __init__(self, name, breed):
        self.name = name  
        self.breed = breed

    def bark(self):
        print(f"{self.name} of {self.breed} breed says: Woof! Woof!")

dog1 = Dog("Tommy", "German Shepherd")

dog1.bark()

# -------------- P11 --------------
class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total Books: {cls.total_books}")

book1 = Book("Harry Potter")
book2 = Book("Lord of the Rings")
book3 = Book("Taary Zameen Par")

Book.display_total_books()

# -------------- P12 --------------
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")

# -------------- P13 --------------
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()

my_engine = Engine()
my_car = Car(my_engine)

my_car.start_car()

# -------------- P14 --------------
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department_info(self):
        print(f"Department: {self.department_name}")
        self.employee.display()

emp1 = Employee("Omer")
dept = Department("HR", emp1)

dept.show_department_info()

# -------------- P15 --------------
class A:
    def show(self):
        print("A is being shown")

class B(A):
    def show(self):
        print("B is being shown")

class C(A):
    def show(self):
        print("C is being shown")

class D(B, C):
    pass

obj = D()
obj.show()

print("MRO:", [cls.__name__ for cls in D.__mro__])

# -------------- P16 --------------
def log_function_call(f):
    def wrapper():
        print("Function is being called")
        return f()

    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# -------------- P17 --------------
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Muhammad Omer")

print(p.greet())

# -------------- P18 --------------
class Product:
    def __init__(self, _price):
        self.price = _price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be positive number!")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
        print("Price successfully deleted.")

p = Product(100)

print(f"Initial Price: {p.price}")

p.price = 150
print(f"Updated Price: {p.price}")

p.price = -1

del p.price

# -------------- P19 --------------
class Multiplier:
    def __init__(self, fact):
        self.fact = fact

    def __call__(self, value):
        return value * self.fact

multiplier = Multiplier(5)
print("Is multiplier callable?", callable(multiplier))

result = multiplier(10)
print(f"Result of calling multiplier(10): {result}")

# -------------- P20 --------------
class InvalidAgeError(Exception):
    def __init__(self, message = "Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")

    else:
        print(f"Age {age} is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except InvalidAgeError as err:
    print(f"Error: {err}")

# -------------- P21 --------------
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current + 1
        else:
            raise StopIteration

countdown = Countdown(7)

for number in countdown:
    print(number)
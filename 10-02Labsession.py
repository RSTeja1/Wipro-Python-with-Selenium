#1
# Base class
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Employee Salary:", self.salary)
        return self.salary


# Child class (Overriding method)
class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    # Method overriding
    def calculate_salary(self):
        total = self.salary + self.bonus
        print("Manager Salary (with bonus):", total)
        return total


# Runtime Polymorphism (Parent reference, Child object)
emp = Employee(30000)
mgr = Manager(50000, 10000)

# Parent reference
ref = mgr      # Employee reference pointing to Manager object
ref.calculate_salary()   # Calls Manager's method (runtime)

#2
# Class Dog
class Dog:
    def speak(self):
        print("Dog says: Woof!")

# Class Cat
class Cat:
    def speak(self):
        print("Cat says: Meow!")

# Class Cow
class Cow:
    def speak(self):
        print("Cow says: Moo!")

# Polymorphic function
def animal_sound(obj):
    obj.speak()   # Same function call, different behavior

# Main program
d = Dog()
c = Cat()
cw = Cow()

animal_sound(d)
animal_sound(c)
animal_sound(cw)

#3
# Base class
class Vehicle:
    def fuel_type(self):
        print("Vehicle uses fuel")

# Derived class 1
class Car(Vehicle):
    def fuel_type(self):
        print("Car uses petrol or diesel")

# Derived class 2 (Multilevel Inheritance)
class ElectricCar(Car):
    def fuel_type(self):
        print("Electric Car uses electricity")

# Main program (Polymorphism demonstration)
v = Vehicle()
c = Car()
e = ElectricCar()

# Calling same method with different objects
v.fuel_type()
c.fuel_type()
e.fuel_type()

#4
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Overloading + operator
    def __add__(self, other):
        return self.balance + other.balance

    # Overloading > operator
    def __gt__(self, other):
        return self.balance > other.balance

    # Display function
    def show(self):
        print("Balance:", self.balance)


# Create objects
acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

# Display balances
acc1.show()
acc2.show()

# Using overloaded + operator
total = acc1 + acc2
print("Total Balance:", total)

# Using overloaded > operator
if acc1 > acc2:
    print("Account 1 has more balance")
else:
    print("Account 2 has more balance")

#5
# Base Class
class A:
    def show(self):
        print("This is class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("This is class B")

# Class C inherits from A
class C(A):
    def show(self):
        print("This is class C")

# Class D inherits from both B and C (Diamond Structure)
class D(B, C):
    pass


# Create object of D
obj = D()
obj.show()

# Display MRO
print(D.mro())

#6
# Parent Class
class Calculator:
    def divide(self, a, b):
        return a / b   # Normal division


# Child Class (Method Overriding)
class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"


# Demonstration
c = Calculator()
s = SafeCalculator()

print("Calculator Result:", c.divide(10, 2))
print("SafeCalculator Result:", s.divide(10, 0))   # Polymorphism in action

#7
# Base Class
class Payment:
    def pay(self, amount):
        print("Processing payment of:", amount)


# Child Classes
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")


# Polymorphic Function
def process_payment(payment_method, amount):
    payment_method.pay(amount)


# Main Program
cc = CreditCard()
upi = UPI()
nb = NetBanking()

process_payment(cc, 1000)
process_payment(upi, 500)
process_payment(nb, 2000)




























































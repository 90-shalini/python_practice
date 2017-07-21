'''
    Normal Inheritance
'''

class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def name(self):
        return self.firstName + self.lastName

class Employee(Person):
    def __init__(self, first, last, staffNum):
        Person.__init__(self, first, last)
        self.staffNumber = staffNum

    def GetEmployee(self):
        return self.name() + ", " + self.staffNumber

x = Person("Shalini"," Arora")
y = Employee("Vibhor"," Jain", "507")

# print(x.name())
# print(y.GetEmployee())

# '''
# Overloading and overriding
# '''



class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def __str__(self):
        return self.firstName + self.lastName

class Employee(Person):
    def __init__(self, first, last, staffNum):
        super().__init__(first, last)
        self.staffNumber = staffNum

x = Person("Shalini"," Arora")
y = Employee("Vibhor"," Jain", "507")


print("Overloading and overriding:")
print(x)
print(y)

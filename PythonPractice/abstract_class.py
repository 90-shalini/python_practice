from abc import ABCMeta, abstractmethod

class baseClass:
    

    @abstractmethod
    def printName(self):
        print("I am abstract method")

class childClass(baseClass):
    def printName(self):
        print("I am in child class")

obj = baseClass()
obj.printName()

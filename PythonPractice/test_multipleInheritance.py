class vehicle():
    def __init__(self):
        print("In class base1 vehicle: ")

    def getType(self, type):
        print("This is ",type, "vehicle.")

class maruti:
    def __init__(self):
        print("In class base2 maruti:")

    def getModel(self, model):
        print("I am maruti ",model)

class bike(maruti, vehicle):
    def __init__(self):
        super().__init__



obj = bike()
obj.getModel('swift')
obj.getType('car')

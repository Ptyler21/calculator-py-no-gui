
import string
import logging
import sys

logging.basicConfig(level=logging.DEBUG,filename="example.log")

class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.choice = int(input("Please give me choice: "))
        logging.debug("Operation Created: x = {} and y={}".format(self.x,self.y))

    def addition(self):
        additionOperation = self.x + self.y
        logging.debug("adding {} + {} , expected result = {}".format(self.x,self.y,additionOperation))
        return additionOperation

    def subtraction(self):
        subtractionOperation = self.x - self.y
        logging.debug("subtracting {} - {}, expected result = {}".format(self.x,self.y,subtractionOperation))
        return subtractionOperation

    def division(self):
        divisionOperation = self.x / self.y
        logging.debug("dividing {} / {}, expected result = {}".format(self.x,self.y,divisionOperation))
        return divisionOperation

    def mulitply(self):
        multiplyOperation = self.x * self.y
        logging.debug("multiplying {} * {}, expected result = {}".format(self.x,self.y,multiplyOperation))
        return multiplyOperation

    def printoption(self):
        print(self.choice)
        logging.debug("user chose {}".format(self.choice))
        if int(1) == self.choice:
            print(self.addition())
        elif int(2) == self.choice:
            print(self.subtraction())
        elif int(3) == self.choice:
            print(self.division())
        elif int(4) == self.choice:
            print(self.mulitply())
        else:
            print("Non-valid option")
            sys.exit(0)


tree = calculator(3,4)

tree.printoption()
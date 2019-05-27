
import string
import logging
import sys

logging.basicConfig(level=logging.DEBUG,filename="example.log")

class calculator:
    def __init__(self):
        self.x = int(input("give me the first number: "))
        self.y = int(input("give me the second number: "))
        self.choice = int(input("Please give me choice: "))
        self.loop = True
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
        #userSecondChoice = input("second")

        loopChoice = self.choice
        logging.debug("user chose {}".format(loopChoice))
        if int(1) == loopChoice:
            print(self.addition())
        elif int(2) == loopChoice:
            print(self.subtraction())
        elif int(3) == loopChoice:
            print(self.division())
        elif int(4) == loopChoice:
            print(self.mulitply())
        else:
            print("Non-valid option")

class addCalc:
    def __init__(self):
        self.newlist = newlist = {}

def main():
    live = []
    tree = calculator()

    tree.printoption()

    objs = [calculator() for i in range(10)]
    for obj in objs:
        live.append(obj)

    objs[2].printoption()

if __name__ == "__main__":
    main()
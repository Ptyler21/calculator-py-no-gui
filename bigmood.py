
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

    def multiplePrint(self):
        userCont = True
        #userSecondChoice = input("would you like to go again?(y/n): ").strip()
        userInt = 0
        while userCont:
            userSecondChoice = input("would you like to go again?(y/n): ").strip()
            if "n" == userSecondChoice:
               print("Good bye!")
               userCont = False
               sys.exit(0)
            elif "y" == userSecondChoice:
               userInt += 1
               live = []
               objs = [calculator().printoption() for i in range(userInt)]
               for obj in objs:
                   live.append(obj)
            pass

class addCalc:
    def __init__(self):
        self.newlist = newlist = {}

def main():
    tree = calculator()

    tree.printoption()
    tree.multiplePrint()



if __name__ == "__main__":
    main()
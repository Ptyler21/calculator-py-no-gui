
import string
import logging
import sys

logging.basicConfig(level=logging.DEBUG,filename="example.log")

class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
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

        ans = True
        while ans:
            self.x = int(input("Give me the first number: "))
            self.y = int(input("Give me the second number: "))
            ans = input("make a choice (1-4), press 5 to exit: ")
            logging.debug("user chose {}".format(ans))
            if "1" == ans:
                print(self.addition())
                userExitChoice = input("Would you like to continue y/n: ")
                if "y" == userExitChoice:
                    continue
                else:
                    break
            elif "2" == ans:
                print(self.subtraction())
                userExitChoice = input("Would you like to continue y/n: ")
                if "y" == userExitChoice:
                    continue
                else:
                    break
            elif "3" == ans:
                print(self.division())
                userExitChoice = input("Would you like to continue y/n: ")
                if "y" == userExitChoice:
                    continue
                else:
                    break
            elif "4" == ans:
                print(self.mulitply())
                userExitChoice = input("Would you like to continue y/n: ")
                if "y" == userExitChoice:
                    continue
                else:
                    break
            elif "5" == ans:
                print("Thank you for using the calculator!")
                sys.exit(0)
            else:
                print("Non-valid option")

def main():
    tree = calculator(3,4)
    tree.printoption()


if __name__ == "__main__":
    main()
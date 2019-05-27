
import string
import logging
import sys

logging.basicConfig(level=logging.DEBUG,filename="examplelog")
def addOperation(x,y):
    addition = x + y
    return addition

def subOperation(x,y):
    subtraction = x - y
    return subtraction

def multiplicationOperation(x,y):
    multiply = x * y
    return multiply

def divisionOperation(x,y):
    divide = x/y
    return divide


print("please pick you operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    userInput = int(input("please input a number: ").strip())
except ValueError:
    logging.DEBUG("exiting system with input {}".format(userInput))
    


# -*- coding: utf-8 -*-
"""
author:Dan
"""

#Question1 


def inputRadius():
    
    while True:
        try:
            radius = float(input ("Enter radius: "))
            break
        except:
            print("Input must be an float! Please try again!")
    return radius   


        
def calculateCircumferinceAndArea():
    pi = 3.142
    test = "y"
    while(test == "y"):
        num = 1
        radius = inputRadius()
        print("Circumference: " + str(2*(pi * radius)))
        print("Area: " + str(pi * (radius ** 2)))
        num = num + 1
        
        test = str(input("Continue? (y/n): "))
        
        if (test != "y" and test == "n") :
            print("Goodbye. You created " + str(num) + " Circle(s).")
        
        
    
    

def main():
     
    print("Welcome to the Circle App")
    calculateCircumferinceAndArea()
    
if __name__ == "__main__":
    main()       
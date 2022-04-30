# -*- coding: utf-8 -*-
"""

"""

#Question 

def inputAmount():
    
    while True:
        try:
            amount = float(input ("Enter amount: "))
            break
        except:
            print("Input must be an float! Please try again!")
            
        
    return amount   

def replay():
    
     test = str(input("Continue? (y/n): "))
    
     return test
   
def calculateTax(amount,amount2,amount3):
    
    if (amount < 11000 or amount2 <11000 or amount3 < 11000):
        
        taxAmount = amount * 0.2
        taxAmount1 =amount2 * 0.2
        taxAmount2 =amount3 * 0.2
        totalTax  = taxAmount + taxAmount1 + taxAmount2
   
    if ((amount > 11000.01 and amount < 25000.00) or (amount2 > 11000.01 and amount2 < 25000.00) or (amount3 > 11000 and amount3 < 25000.00)):
        taxAmount = amount * 0.3
        taxAmount1 = amoun2 * 0.3
        taxAmount2 = amount3 * 0.3
        totalTax1  = taxAmount + taxAmount1+taxAmount2
    else:
        totalTax1 = 0.00
        
    if (amount > 25000.00 or amount2 > 25000.00 or amount3 > 25000.00):
        taxAmount = amount * 0.4
        taxAmount1 = amount2 * 0.4
        taxAmount2 = amount3* 0.4
        totalTax2  = taxAmount + taxAmount1 + taxAmount2
    else:
        totalTax2 = 0.00
        
    print ("Your Tax Liability is: -20% tax rate: " + str(totalTax) + ", 30% tax rate: " + str(totalTax1) + ", 40 % tax rate : " +str(totalTax2) )
            
    print ("Total Tax Liability: -" + str(totalTax + totalTax1 +totalTax2 ))
    
def main():
    
     
    print("Welcome to the Tax Application")
    
    amount = inputAmount()
    num = 0
    rep = replay()
    num = num + 1
    if rep == "y":
        amount2 = inputAmount()
    num = num + 1
    rep = replay()
    
    if rep == "y":
        amount3 = inputAmount()
    num = num + 1
    rep = replay()
    if rep == "n":
        calculateTax(amount,amount2,amount3)
    print("Goodbye, you entered " + str(num) + " amounts.")
    
if __name__ == "__main__":
    main() 



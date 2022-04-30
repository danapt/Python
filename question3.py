# -*- coding: utf-8 -*-


#question3

def replay():
    
    test = str(input("Continue? (y/n): "))
    
    return test

def inputAge(n):
    
    while True:
        try:
            lst = []
            
            for i in range(0, n): 
                ele = int(input ("Enter Age: ")) 
  
                lst.append(ele) # adding the element 
                
                rep = replay()
                if rep == "n":
                    break
            
            break
        except:
            print("Input must be an integer! Please try again!")
                
    return lst   


def calculateAge(lst):
    
    print("List of Ages is: ", lst)
    lst.sort()
    print ("Sorted List of Ages is: ", lst)
    print ("Max age is: " , max(lst))
    print ("Min age is: " , min(lst))
    average = sum(lst)/len(lst)
    print ("Average Age: ", str(average))
          
    
           
    
def main():
    
    print("List of Ages")
    
    n = int(input("Enter number of elements : ")) 
    
    lst = inputAge(n)
    
    calculateAge(lst)
    
    print("Goodbye, you entered " + str(n) + " ages.")
    
if __name__ == "__main__":
    main() 
#perfect number
#In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# easy code to check if a number is perfect
#daniel apetri
#win 10 18.09.2017

#input from the user
number = int(input("enter a number: "))
divisor = 1
sum_divisor=0

#check the factors of the number and add the positive divisors
while divisor<number:
    if number%divisor==0:
        print (divisor,"is a divisor ",end=' ')
        sum_divisor = sum_divisor + divisor
    divisor+=1

print("\n")
#check if the number is a perfect number
if number==sum_divisor:
    print(number,"is a perfect number")
else:
    print(number,"is not a perfect number")




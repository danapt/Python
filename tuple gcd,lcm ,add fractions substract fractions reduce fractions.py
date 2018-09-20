#work with tuple and gcd,lcm ,add fractions substract fractions reduce fractions
#danile Apetri

#function to find the greatest common divosor(GCD OR HCF(highest common factor))
def gcd(a,b):

    while b!=0:
        temp = b
        b = a%b
        g = temp

    return g

#function to find the least common multiple(LCM)
def lcm(a,b):

    #call function to find the greatest common divisor of this 2 numbers
    g = gcd(a,b)
    lcm = int((a*b)/g)
    return lcm


#function to add 2 fractions
def addfractions(a,b,c,d):

    denominator = lcm(b,d)
    num1 = denominator / b*a
    num2 = denominator /d*c
    numerator = num1 + num2
    #function to find the gcd of the numerator and denominartor
    g = gcd (numerator,denominator)

    tuple = (int(numerator/g),int(denominator/g))

    return tuple

#function to substract 2 fractions
def subtract_fractions(a,b):

    denominator = lcm(a[1],b[1])
    num1 = denominator / a[1]*a[0]
    num2 = denominator /b[1]*b[0]
    numerator = num1 - num2
    g = gcd (numerator,denominator)

    tuple = (int(numerator/g),int(denominator/g))

    return tuple

def reduce_fraction(a):
    g = gcd(a[0],a[1])
    reduce = (int(a[0]/g),int(a[1]/g))

    return reduce

from fractions import *

def main():

    print("enter your tuple to find the gcd:",)
    t_list = tuple(int(x) for x in input().split(','))

    print(t_list)

    a = t_list[0]
    b = t_list[1]

    #function to find the gcd
    gst_com_div = gcd(a,b)

    print("greates common divisor is:", gst_com_div)

    print("enter your tuple to find the lcm:", )
    t_t = tuple(int(x) for x in input().split(','))

    #function to find the lcm
    l_c_m = lcm(t_t[0],t_t[1])
    print("least common multiple is:",l_c_m)

    print("enter 1st fraction with , after 1st number:",)
    frac1 = tuple(int(x) for x in input().split(','))
    print("enter 2nd fraction:",)
    frac2= tuple(int(x) for x in input().split(','))
    #function to
    fract = addfractions(frac1[0],frac1[1],frac2[0],frac2[1])

    print(fract)
    #function to subtract 2 fractions
    fract_sub = subtract_fractions(frac1,frac2)
    print (fract_sub)

    print("enter a fraction to be reduce")
    reduce_frac = tuple(int(x) for x in input().split(','))

    rec_frac = reduce_fraction(reduce_frac)
    print("reduce fraction is:",rec_frac)

    #import fraction for checking fractions
    print("\nfractions adding and subtarct")
    a = Fraction(11,3)
    b = Fraction(45,23)
    print(a+b)
    print(a-b)

    return 0
main()





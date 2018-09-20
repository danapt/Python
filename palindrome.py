#program to check if a string is a palindrome 
#daniel apetri
#28.09.2017

def main():

    string = input("enter your string:")
    string_rev = string[::-1]

    if string == string_rev:
        print("the string is a palindrome:")
    else:
        print("the string is not a palindrome:")

main()

def isapalindrome():

    str=input("enter your string:")
    s1=str.lower()

    if s1 == s1[::-1]:
        print("palindrom")
    else:
        print("not palindrome")

isapalindrome()
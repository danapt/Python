#add items to a list from the user using comprehension
#daniel apetri
#win 10
#10.10.2017

def list_integer():

    print("enter your integers in the list and after  press space:",)
    lst = [int(n) for n in input().split()]
    #a = [int(x) for x in input().split()]
    print(lst)

list_integer()

def shopping_list():

    size = int(input("how long you want the list: "))
    list = [0]*size
    for i in range(size):
        list[i] = input("enter your item in the list:")

    print(list)
shopping_list()
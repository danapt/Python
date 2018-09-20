#bubble sort in python
#daniel

#function to swap elements in a list
'''def swap(a,b):

    a,b = b,a

    return (a,b)'''

#function to sort the elements in a list because a list is mutable and you can do it
def bubblesort(l):


    for i in range(len(l)):
        num = 0
        for j in range((len(l)-1-i)):
            if l[j] > l[j+1]:
                #l = swap(l[j],l[j+1])
                l[j],l[j+1] = l[j+1],l[j]
                num = 1

        if (num == 0):
            break

    print(l)

def main():

    # input from the keybord the elements in the list
    print("enter your numbers and press space after every input:")
    lst = [int(elements) for elements in input().split()]
    print(lst)

    #alternative input in a list
    """size = int(input("enter size of the list:"))
    lst = [0]*size
    for i in range(size):
        lst[i] = int(input("enter digit:"))"""

    #call the bubblesort() function
    bubblesort(lst)


main()



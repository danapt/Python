# fibbonaci
# apetri daniel
#win10

def main():
    num = 0
    num2 = 1
    sequence= int(input("enter how many numbers you want in the sequence: "))

    print(num,num2,end=" ",)

    while (sequence-2 > 0):
        new = num + num2
        print(new,end=" ",)
        num = num2
        num2 = new
        sequence = sequence-1
main()

#perfect number in a range
#danile apetri
#18.09.2017


# input from the keyboard
top_num=int(input("enter the last number in the range:"))
number=2

# loop that will iterate form number =2 to the input
while number<=top_num:
    sum=0
    div=1

    #find the divisors and add in sum
    while div<number:
        if number%div==0:
            sum=sum+div
        div+=1
    # check if perfect , abundant or deficient
    if number == sum:
        print(number, "is perfect")
    elif number < sum:
        print(number, "is abundant")
    else:
        print(number, "is deficient")

    number+=1



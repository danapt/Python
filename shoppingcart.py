#dictionary with products in a shop
#add, remove and do all the things a customer can do in a shop
#author: Daniel Apetri
#tutorial 8 shopping cart

def add_products(dict_cart):


    key = input("enter your product: ")
    amount = int(input("enter the amount: "))
    price = float(input("enter price: "))

    a=0
    #dict_cart.setdefault(key, [])

    #dict_cart[key].append(amount)

    #dict_cart[key].append(price)

    #if you want to add more produst as the same type add the amount
    for i,j in dict_cart.items():

        if i == key:
            j[0]= j[0] + amount
            a=1

    if a == 0:

        dict_cart.setdefault(key, [])

        dict_cart[key].append(amount)

        dict_cart[key].append(price)






    print(dict_cart)


def show_products(list):

    for key,value in list.items():
        print("the product is: ",key)
        print("the amount of items in the shopping cart are: ",value[0])
        print("the price for one item is :", value[1])
        print ("\n")


def remove_product(list):

    remove = input("\nenter the product you want to remove: ")

    for i,j in list.items():
        if i == remove:
            amount = int(input("enter the amount you want to put it back in the shop: "))
            if j[0] >= amount:
                j[0] = j[0] - amount
            elif j[0] < amount:
                print("the amont you enter is wrong ! "
                      "YOu can't enter a value bigger than you have in the shopping cart!")
                break
                if j[0] == 0:
                    list.pop(i,None)
                    break
                break
            else:
                print("you must enter a amount less or equal to your amount product!!!")
            list.pop(i,None)
            return




def sum_of_products(list):

    sum = 0
    for key,value in list.items():
            sum = sum + value[0]*value[1]
    print("the sum you have to pay is: ",sum,"euros")


def main():

    #shopping_cart = {"apple": [10,0.50],"bananas": [1200,0.30],"beef meat": [100,7.00],"onion":[1000,0,05]}
    shop_cart = {}

    gandul = 0


    while gandul == 0:
        print("1. add products in the cart and specify the price and the amount\n"
              "2. remove products from the cart\n"
              "3. see the total price of the cart\n"
              "4. display the products in teh shopping cart\n"
              "5. exit\n")

        # statemnet to check if the shopping cart is empty or not
        isempty = bool(shop_cart)
        #variable to select the menu
        choice = int(input("enter your option from the menu: "))

        if choice == 1:
            add_products(shop_cart)
        elif choice == 2:
            if isempty == True:
                remove_product(shop_cart)
            else:
                print ("the shopping cart is empty and need to press option 1 to add some products")
        elif choice == 3:
            sum_of_products(shop_cart)
        elif choice == 4:
            if isempty == True:
                show_products(shop_cart)
            else:
                print ("the cart is empty!")
        elif choice == 5:
            gandul == 1
            exit()
        else:
            print("your option is wrong "
                  "please choose again from the menu\n")

if __name__ == '__main__':
    main()

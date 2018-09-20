#the hang man in python
#Author: Daniel Apetri
#date : 19.10.2017

from random import*

def main():

    name = input("enter your name:")
    count = 0

    print("thanks for playing,",name,",the game will start now!")
    print("if you have 6 mistakes you lose")

    """print("enter your word and press space after every letter")
    word = [string for string in input()]
    print(word)"""
    word_list = ['secret','dublin','jon','gandul','institute']

    y = randint(0, len(word_list)-1)
    print(y)

    word = word_list[y]
    #print(word)
    word1 = word

    print("you have ,",len(word),",guesses")
    guesses =len(word)
    failed = 6

    wrong = 0
    mistakes = 6
    count = 0
    print(word)

    while (((wrong < mistakes)) and ((count <len(word)))):
        guess = (input("enter your letter:"))
        i = 0
        x = 0
        for i in range(len(word1)):
            if (word1[i] == guess):
                x = 1
                fi = word1.find(guess)
                word1 = word1[:fi] + word1[fi + 1:]

                print(word1)
                #word.remove(word[i])
                break
            x = 2

        if (x == 1):
            print("you guess right\n")
            count += 1
        else:
            failed -= 1
            print("you are wrong!,you have left:",failed," guesses\n")
            wrong +=1

    if (wrong == mistakes):
        print("End of the game!")
        print("you lose!")


    if (count ==len(word) ):
        print("you guess,",count,"times the letter\n")
        print("you won!\n")


if __name__ == '__main__':
    main()

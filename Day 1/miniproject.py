# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:27:18 2019

@author: Saqeeb
"""

from random import randint


secret_number=(randint(1,9))
i=0
while i<6:
    flag=True
    guess=input("Guess a number = ")
    if not guess:
        print("Loser")
        break
    if guess not in "1234567890":
        print("Enter a integer\nLoser")
    else:
        guess=int(guess)
        if (secret_number == guess ):
            print("Winner")
            break
        elif (secret_number-guess>4 or secret_number-guess<-4):
            print("too high")
        elif (secret_number-guess<2 and secret_number-guess>-2):
            print("too close")
        else:
            print("Wrong")
        if i==5:
            print("Loser")
            print("secret number is " + str(secret_number))
            break
        if i<5:
            play_again=input("play again any or n : ")
            if play_again=="n":
                print("Loser")
                break
    i=i+1
    print("-----------------------------\nNumber of tries left "+str(6-i) )
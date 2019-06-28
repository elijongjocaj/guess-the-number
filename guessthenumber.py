#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1


uname = input("Hello, What is your username?")

print("Hello", uname + ".",)

question = input("Would you like to play a game?[Yes/No)")
if question == "No":
   print("oh... okay")

if question == "Yes":
   print("I'm thinking of a number between 1 and 10")
   guess = int(input("Have a guess"))
   if guess > number:
       print("guess lower...")
   if guess < number:
      print("guess higher...")
   while guess != number:
       tries += 1
       guess = int(input("You lost, try again!:"))
       if guess > number:
           print("Guess lower...")
       if guess == number:
        print("You'r right! You win! The number was", number,\
              "and it only", tries, "tries!")

        


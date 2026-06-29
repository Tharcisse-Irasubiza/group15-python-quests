#!/usr/bin/python3
# Quest 22: The Personalized Scroll
# Goal: Create a function with parameters, then call it using user input.

def personalized_greeting(name, quest):
    print("Greetings, " + name + "! Your quest is: " + quest)

user_name = input("Enter your name: ")
user_quest = input("Enter your quest: ")

personalized_greeting(user_name, user_quest)

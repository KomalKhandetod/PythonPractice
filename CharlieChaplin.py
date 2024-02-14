# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
answer = ["Bristol", "Birmingham","London","Exeter"]

def main():
    print(answer)
    userAnswer = input("Where was Charlie Chaplin born?")
    chaplin(userAnswer)

def chaplin(userAnswer):
    if(userAnswer in answer):
        if(userAnswer == "Birmingham"):
            print("Correct!")
        else:
            print("Incorrect Answer")
    else:
        print("Entered value is not present in the options mentioned above!")
main()
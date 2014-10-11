#!/usr/bin/python

# Week 2 Problem 1

# Write a very simple program that asks the user to enter his or her name,
# and prints out a welcome message that is customized to the user's name.
# For example, the program should wait for the user's input after printing out

# Enter your name:

# When you enter your name,

# Enter your name: World

# the output on the next line should be

#     Hello, World!

# Rename this file using your name.
# Make the file executable.
# Use input() or raw_input() function to accept an input from the user
# and store it in a string variable.
# Use print() function to print the welcome message on the screen.

# Use Python 3 print() format
from __future__ import print_function

def welcome():
	name = input("Enter your name:")
	print("Hello, " + name + "!")
	
	return None


    
if __name__ == "__main__":

    welcome()

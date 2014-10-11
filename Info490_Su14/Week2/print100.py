#!/usr/bin/python

# Week 2 Problem 2. A famous simple interview question.

# Print every number from 1 to 100.
# If the number is a multiple of 4, print "info" instead.
# If the number is a multiple of 6, print "matics" instead.
# If the number is a multiple of 4 and 6, print "informatics" instead.

# Make the file executable.
# Write a function named list_informatics() that takes no argument and returns
# a list of strings. (Use str() to convert numbers into strings.)
# The print function must appear only once in your program in the main() function.

# Rename this file using your name.

# Use Python 3 print() function
from __future__ import print_function

def list_informatics():
    
    '''
    Returns a list of strings.

    >>> print(list_informatics())
    ['1', '2', '3', 'info', '5', 'matics', '7', 'info', '9', '10', '11', 'informatics', '13', '14', '15', 'info', '17', 'matics', '19', 'info', '21', '22', '23', 'informatics', '25', '26', '27', 'info', '29', 'matics', '31', 'info', '33', '34', '35', 'informatics', '37', '38', '39', 'info', '41', 'matics', '43', 'info', '45', '46', '47', 'informatics', '49', '50', '51', 'info', '53', 'matics', '55', 'info', '57', '58', '59', 'informatics', '61', '62', '63', 'info', '65', 'matics', '67', 'info', '69', '70', '71', 'informatics', '73', '74', '75', 'info', '77', 'matics', '79', 'info', '81', '82', '83', 'informatics', '85', '86', '87', 'info', '89', 'matics', '91', 'info', '93', '94', '95', 'informatics', '97', '98', '99', 'info']
    '''

    result = []

    ######### WRITE YOUR CODE HERE #########
    for i in range(1,101):
        if i%4 ==0 and i%6 == 0:
            result.append ("informatics")
        elif i%4 == 0:
            result.append("info")
        elif i%6 == 0:
            result.append("matics")
        else:
            result.append(i)
    return result



if __name__ == '__main__':

    ######### WRITE YOUR CODE HERE #########
    print (list_informatics())

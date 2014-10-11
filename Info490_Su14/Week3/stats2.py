#!/usr/bin/python

# Week 3 Assignment Problem 1
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

# use Python 3 print() function
from __future__ import print_function, division
# use get_stats() function from week 2 problem 3
from stats import get_stats

def get_column(filename, n, header = True):
    '''
    Returns a list from reading the specified column in the CSV file

    Parameters:
      filename(str): Input file name in Comma Separated Values (CSV) format
      n(int): Column number. The first column starts at 0. The column must be
              a list of integers.
      header(bool): If True, the first line of file is column names. Default: True.

    Examples:
    >>> get_column('ss12pil.csv', 1)[:10]
    [38, 38, 38, 51, 83, 83, 83, 104, 104, 104]
    >>> get_column('ss12pil.csv', 2)[-10:]
    [1, 1, 2, 1, 1, 2, 3, 4, 1, 2]
    '''
    result = []

    # your code goes here
    with open(filename, 'r') as csv_file: #streams in the file will automatically close with the "with" statement
        if header == True: #checks to see if there is a header
            next(csv_file) #if there is a header skips that line
        for line in csv_file: #loops through each row in the file
            row= line.split(',') #turns each line into a list of strings called row
            if row[n] == '': #checks to see if any elements in that row are empty string 
                result.append(0) # if so we will insert a zero at the index
            else:
                result.append(int(row[n])) #else just add the element of that index. Cast the string as a int because we need a list of intergers to do the stats operation
                            
    
    return result

def print_stats(input_list, title = None):
    '''
    Computes minimum, maximum, mean, and median using get_stats function from
      stats module, and prints them out in a nice format.

    Parameters:
      input_list(list): a list representing a column
      title(str): Optional. If given, title is printed out before the stats.

    Examples:
    >>> print_stats(range(50))
    Minimum: 0
    Maximum: 49
s    Mean: 24.5
    Median: 24.5
    >>> print_stats(range(100), 'Stats!')
    Stats!
    Minimum: 0
    Maximum: 99
    Mean: 49.5
    Median: 49.5
    '''

    # your code goes here
    if title == None: #checks to see if there is a title
        print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" %get_stats(input_list)) #if not just print the statistics
    else: #if there is a title
        print(title)#print the title
        print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % get_stats(input_list))#then print the statitics
    
    return None
    
if __name__ == '__main__':

    # your code goes here
    column_seven = get_column('ss12pil.csv',7,True)
    print_stats(column_seven,"Column 7")
    
    column_eight = get_column('ss12pil.csv',8,True)
    print_stats(column_eight,"Column 8")
    
    column_eight = get_column('ss12pil.csv',40,True)
    print_stats(column_eight,"Column 40")
    
    column_last = get_column('ss12pil.csv',73,True)
    print_stats(column_last,"Column 73")
    
                
    


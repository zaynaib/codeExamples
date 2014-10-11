#!/usr/bin/python

# Week 3 Assignment Problem 3
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

# use Python 3 print() function
from __future__ import print_function, division
import numpy as np

def get_columns(filename):
    '''
    Takes a file and returns a 2-D numpy array of columns 6, 7, 39, and 72.

    Parameters:
      filename(str): the name of the CSV file
    Examples:
    >>> get_columns('ss12pil.csv').shape
    (4, 127208)
    >>> get_columns('ss12pil.csv')[0, :10]
    array([ 200.,   70.,  212.,   15.,   71.,   80.,   95.,  131.,  147.,  149.])
    '''
    
    result = np.loadtxt(filename,delimiter = ',',converters = {39: lambda x: float(x or 0), 72: lambda x: float(x or 0)}, skiprows = 1, usecols=(6,7,39,72) )
    '''we use np.loadtxt() to load the a file and use the optional parameters to format the file.
       In this case our delimiter are commas, use the lambda function as our converter to change all the empty strings into 0 and the non empty strings into floats
       skiprows  = 1 because we want to get skip over the header
       usecols is self explanatory 
    '''
    result = np.transpose(result)
        
    return result
    
def print_stats(input_array, title = None):
    '''
    Computes minimum, maximum, mean, and median using numpy functions,
      and prints them out in a nice format.

    Parameters:
      input_array(numpy.ndarray): a numpy array representing a column
      title(str): Optional. If given, title is printed out before the stats.

    Examples:
    >>> import numpy as np
    >>> print_stats(np.array([1, 2, 3, 4, 5]))
    Minimum: 1
    Maximum: 5
    Mean: 3.0
    Median: 3.0
    >>> print_stats(np.array([1, 2, 3, 4, 5, 6]), 'Stats!')
    Stats!
    Minimum: 1
    Maximum: 6
    Mean: 3.5
    Median: 3.5
    '''

    # your code goes here
    minimum = np.amin(input_array)          #this function finds the minimum number of the array
    maximum = np.amax(input_array)          #this funtion find the maxium number of the array
    mean = np.mean(input_array)             # this function finds the mean of the array 
    median = np.median(input_array)         # this function find the median of the array
    stats = minimum,maximum, mean, median   # creates a tuple called stats that holds in all the descriptive statsitics
    if title == None: #if there is no title
        print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % stats)  #Print the stats tuple
    else: #if there is a title
        print(title) #print the title
        print("Minimum: %i\nMaximum: %i\nMean: %.1f\nMedian: %.1f" % stats) #print the stats tuple
        
    
    return None
    
if __name__ == '__main__':
    
    # your code goes here
    col = get_columns('ss12pil.csv') #get the columns from the csv file
    print_stats(col) #prints out the descriptivve statisctis  
	

    

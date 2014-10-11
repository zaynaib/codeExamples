#!/usr/bin/python

# Week 7 problem 1. PMF, PDF, and CDF.

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.
# Do not import other modules other than the ones listed here.

from __future__ import print_function, division
import matplotlib.pyplot as plt
import numpy as np
from stats2 import get_column

def get_histogram(sequence):
    '''
    Takes a list and returns a dictionary of the form {value: frequency}.

    Examples:
    >>> get_histogram(['a', 'a', 'b', 'b', 'b', 'c'])
    {'a': 2, 'b': 3, 'c': 1}
    >>> get_histogram([4, 5, 6, 6, 6])
    {4: 1, 5: 1, 6: 3}
    '''
    hist = {}

    # your code goes here
    for w in sequence: #iterates through the list given
        if w not in hist: #if the word is new the freq is 1
            hist[w] =1
        else:  #if the word already exists add to the freq
            hist[w] =hist[w] +1
    
    return hist

def get_pmf(sequence):
    '''
    Takes a list and returns a dictionary of the form {value: probability}.

    Examples:
    >>> get_pmf(['a', 'a', 'b', 'b', 'b', 'c'])
    {'a': 0.3333333333333333, 'b': 0.5, 'c': 0.16666666666666666}
    >>> get_pmf([4, 5, 6, 6, 6])
    {4: 0.2, 5: 0.2, 6: 0.6}
    '''
    pmf = {}
    
    # your code goes here
    pmf = get_histogram(sequence) #finds the freq of the list given
    for key, value in pmf.items(): #iterates through the dictionary items
        pmf[key] = value/len(sequence) #changes the value of the key to the probability

    return pmf
    
def get_cdf(sequence):
    '''
    Takes a Numpy array and returns a tuple that represents
    the x and y axes of the empirical distribution function.

    Examples:
    >>> import numpy as np
    >>> x = np.array([4, 3, 1, 2, 5])
    >>> get_cdf(x)
    (array([1, 2, 3, 4, 5]), array([ 0.2,  0.4,  0.6,  0.8,  1. ]))
    '''

    # your code goes here
    x = np.sort(sequence) #sorts the x array
    length = sequence.size #gives you the length of the array size
    y = np.arange(1,length+1) 
    z = np.arange(1,length+1)
    z.fill(length)  #fill the array with the number n
    z = z.astype(float) #turns the elements into floats
    y = np.divide(y,z)  # divides the sequences 1/n, 2/n ...
    
    return x, y

if __name__ == '__main__':

    filename = 'ss12pil.csv'

    # person's age is WKHP, the 72nd column in ss12pil.csv
    hours_worked = get_column(filename, 72)
    # remove people who didn't work (hours == 0) and some outliers
    hours_worked = [h for h in hours_worked if h > 0 and h < 80]
    # The PMF.
    hist = get_pmf(hours_worked)

    # peron's income is PINCP, the 103rd column in ss12pilcsv
    income = np.loadtxt(filename, delimiter = ',', skiprows = 1, usecols = (103, ),
                        converters = {103: lambda x: int(x or 0.0)})
    # remove some outliers (income below $1000)
    income = income[income > 1000]
    # The CDF
    cdf_x, cdf_y = get_cdf(income)
    # The CCDF
    ccdf_x, ccdf_y = cdf_x, 1.0 - cdf_y

    # you code goes here

    fig, ax = plt.subplots()
    histy = hist.values()
    histx = hist.keys()
    plt.bar(histx,histy)
    
    #Set our axis labels and plot title
    ax.set_title("PMF of hours worked per week in IL in 2012")
    ax.set_xlabel("Hours worked per week")
    ax.set_ylabel("Probability")
     
    #CDF
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    ax.plot(cdf_x, cdf_y)

    # Set our axis labels
    ax.set_xlabel("Income ($)")
    ax.set_ylabel("CDF")
    ax.set_title("CDF of income in IL in 2012")
  
    #CCDF
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(ccdf_x, ccdf_y)

    # Set our axis labels
    ax.set_xlabel("Income ($)")
    ax.set_ylabel("CCDF")
    ax.set_title("CCDF of income in IL in 2012")
      
    #Show final result
    
    plt.show()

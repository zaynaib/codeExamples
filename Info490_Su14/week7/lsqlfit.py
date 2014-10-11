#!/usr/bin/python

# Week 7 problem 3. Least squares fit.

# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.
# Do not import other modules.
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def get_lsqfit(x, y):
    '''
    Takes two arrays and returns a tuple of two floats (slope and
    intercept of least squares fit).

    Examples:
    >>> import numpy as np
    >>> x = np.array([0.0, 1.0, 2.0])
    >>> y = np.array([0.0, 2.0, 4.0])
    >>> get_lsqfit(x, y)
    (2.0, 0.0)
    '''

 
    #sample mean of x and of y
      
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    #variance of x

    x_var = np.var(x,ddof=1)

    #covariance of x and of y    

    covMatrix = np.cov([x,y])
    covxy = covMatrix[0,1] 

    #slope 
    slope = covxy/x_var

    #intercept
    intercept = y_mean - (slope * x_mean)

    return slope, intercept

if __name__ == '__main__':
    # your code goes here
  
	
    #pass in column names for each CSV
 
    data = pd.read_csv('ss12pil.csv')
    
    #clean the data replace NAns with 0

    data = data.fillna(0)

    hours_worked = data['WKHP']
    person_income = data['PINCP']
	

    #create plotting environment
	
    fig, ax = plt.subplots()

    #plot the log of x

    ax.set_yscale('log')

    #creates scatter plot
    ax.scatter(hours_worked,person_income)

    #the x range for the best fit line
    x = np.arange(len(person_income))

    #find the slope
    slope,intercept = get_lsqfit(hours_worked,person_income)
    #print(slope)
    #print(intercept)

    
    #data points for the y
    liney = slope*x + intercept
    ax.plot(x, liney,color ='red')
    plt.xlim([0,120])
    ax.set_xlabel("Hours Worked per week")
    ax.set_ylabel("Income ($)")
    ax.set_title("Least Squares Fit of log PINCP vs WKHP in 2012 il")
	
	
    plt.show()



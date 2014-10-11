#!/usr/bin/python

# Week 3 problem 2
# Do not delete the comments.
# Do not chnage the functions names, do not change the input parameters.
# Do not change the return types of the functions.
# Your code goes to the part where it says your code goes here.
# Do not change anything else other than the part where it says your code goes here.

class OnePerson:
    '''
    Represents a row(one person) from the census file.

    Attributes:
      row (list of strings): stores a row representing one person as a list of strings.

    Methods:
      read_line(self, input_file, n)
      print_column(self, n)

    Examples:
    >>> p = OnePerson()
    >>> print(p.read_line('ss12pil.csv', 1)[:10]) 
    ['P', '38', '01', '01602', '17', '1010207', '00200', '50', '1', '']
    >>> p.print_column(0)
    Column 0 is: P
    >>> p.print_column(1)
    Column 1 is: 38
    '''
    def __init__(self):
        
        '''
        Initializer
        '''
        # your code goes here
        row = [] #creates an empty list called row an attribute that will be initialized later
        input_file = None #creates an empty attribute that will be intialized in the read_line funtion
        n =0 #creates a row number (the number is arbitrary )
        return None #returns none because this is an intializer
     
    def read_line(self, input_file, n):
        '''
        Takes the name of the file and the row number 'n',
        stores in the 'row' attribute the list representing the corresponding row,
        and returns that list.
        '''
        # your code goes here
        self.input_file = input_file #assigns the instance of input_file to whatever the user's input into the function
        self.n = n #assigns the instance of row number to whatever the user's input into the function
        count_num = 0 #this is a row counter

        with open(self.input_file,'r') as f: #opens the file to read and automatically closes the function
            for line in f: #for loop that goes through each line of the file
                if count_num ==0: #skips the first line since we know it will be the header
                    pass
                if count_num == self.n: #checks to see if we are at the row number n 
                    self.row = line.split(',') #if so we will create the row into a list of string
                    return self.row #then we will return the row
                count_num = count_num +1 #when the loop continues  the counter will still be increasing
        return None #if we cannot find the column we will return none
    
    def print_column(self, n):
        '''
        Takes the column number 'n' and prints out the corresponding 'column' of
        the 'row' attribute.
        '''
        # your code goes here
        self.n = n # assigns the row number instance to the user's input
        column = str(self.row[n]) #grabs the element that is stored in the column of the row attibute 
        print('Column %d is: %s' %(self.n,column)) #prints out the column number and what is in the column
    
if __name__ == '__main__':
    
    # your code goes here
    person = OnePerson() #creates an instance of person
    number_row = 100 #creates the row number 
    row_of_person = person.read_line('ss12pil.csv',number_row) #get the row from the file and the specified row number
    for i in range(0,10): #for loop that goes through row 0 to 9
        person.print_column(i) #prints the column of the row

def high_and_low(numbers):
    #split the string to an arrary separted by space
    #loop through the array converting each string to an integer
    #or just us the max or min functions
    results = numbers.split(" ")
    results = map(int, results)
    maxi = max(results)
    mini = min(results)
    r_string = str(maxi) + " " +str(mini)
    print r_string

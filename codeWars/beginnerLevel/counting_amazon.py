def count_arara(n):
    #make a dictionary
    # if number is greater than 8  then add on
    result = ''
    dict = {1: 'anane', 2: 'adak', 3: 'adak anane',4:'adak adak', 5:'adak adak anane', 6:'adak adak adak'
           ,7:'adak adak adak anane',8:'adak adak adak adak'};
    if(n > 8 and n%8==0):
        num = n%8
        multiply = n/8
        result = '{} '.format(dict[8])*multiply
        result=result.rstrip()
    elif(n>8 and n%8 !=0):
        num = n%8
        multiply = n/8
        result = '{} '.format(dict[8])*multiply+" " + dict[num]
        result = result.rstrip()
    else:
        result = dict[n]

    return result

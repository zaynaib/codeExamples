def xo(s):
    s= s.lower()
    x = s.count('x')
    o = s.count('o')
    if(x == o):
        return True
    else:
        return False

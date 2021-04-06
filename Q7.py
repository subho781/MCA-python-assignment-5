str = "Python"
def sl(str) : 
    if str == '': 
        return 0
    else : 
        return 1 + sl(str[1:])  
print (sl(str))
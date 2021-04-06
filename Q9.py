def seq(n):
    l=[]
    for i in range(0,n+1):
        item=pow(i,2)+1
        l.append(item)
    return l
n=5
print(seq(n))
def calValue(x):
    return x*x + 1
items = [2,4,3,8,12]
for i in range(len(items)):
    items[i] = calValue(items[i])
print(items)
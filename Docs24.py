# Q23.Write a Python program to find the highest 3 values of
# corresponding keys in a dictionary.
d1 = {'a': 100, 'b': 200, 'c':300,'d':400,'e':500}

a=[]
max=0
for i in d1:
    a.append(d1[i])
    a.sort()
    b=a[:-4:-1]
print("The three higest values are:_",b)
# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for i,j in a.items():
    if j != None:
        b[i]=j
print(b)
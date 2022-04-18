# Q29.Write a Python program to sort a list alphabetically in a dictionary.

a=[]
num=int(input("Enter the number of elements:- "))
for i in range(1,num+1):
    value=(input("Enter the elements:- "))
    a.append(value)
a.sort()
print(a)

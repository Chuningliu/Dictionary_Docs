# Q14.Write a Python program to multiply all the items in a dictionary.

def multiply(a):
    c=1
    for i in a:
       c=c*a[i]
    print("The answer is",c)
a={1: 1, 2: 4, 3: 9}
multiply(a)

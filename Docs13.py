# Q13.Write a Python program to sum all the items in a dictionary.

   
def Sum(a):
    b=[]
    for i in a:
        b.append(a[i])
    c= sum(b)
    return c
a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
print("Sum :",Sum(a))




   

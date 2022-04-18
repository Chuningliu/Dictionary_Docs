# Q15.Write a Python program to remove a key from a dictionary.

# a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# for i in a:
#         print(a[i],end=" ")
        
d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
z=input("Enter the key to delete(a-d):")
if z in d: 
    del d[z]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)

# Q8.Write a Python program to check whether a given key 
# already exists in a dictionary.


def check(b):
    if b in a:
        print(b,'Key is present in the dictionary')
    else:
        print(b,'Key is not present in the dictionary')
b=int(input("Enter the number:- "))
a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
check(b)

    
        
        

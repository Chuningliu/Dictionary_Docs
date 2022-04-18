# Q42.Write a Python program to check all values are same in a dictionary.
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
b={}
for i,j in a.items():
    if j==12:
        print(True)
    elif j==10:
        print(False)
        
    
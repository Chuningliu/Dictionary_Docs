# Q31.. Write a Python program to get the top three items in a shop.
# Expected Output:

# item4 55
# item1 45.5
# item3 41.3

a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
b=[]
for i in a:
    if a[i]>40:
        b=a[i]
        print(i,b)


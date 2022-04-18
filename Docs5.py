# Q5.Write a Python program to sort (ascending and descending) a dictionary by value.

# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
f={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

a=sorted(f.items())
b=sorted(f.items(),reverse= True)
print("Ascending order by value",a)
print("Descending order by value",b)
















# Q20.Write a Python program to check a dictionary is empty or not.
# Write a Python program to combine two dictionary adding values for common keys. 

# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# SAME AS QUESTION NUMBER 1

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:
    if i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
print(d1)
     




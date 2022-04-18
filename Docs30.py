# Q30.Write a Python program to remove spaces from dictionary keys.
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
for i in a:
    if " " in a:
        a=replace(" ","")
print(a)

# Q22. Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary. Go to the editor
# Expected Output:
# ac
# ad
# bc
# bd

a={'1':['a','b'], '2':['c','d']}
for x in a['1']:
    for y in a['2']:
        print(x + y)
        

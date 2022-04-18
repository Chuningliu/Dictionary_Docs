# Q39.Write a Python program to filter a dictionary based on values. 

# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
b={}
for i,j in a.items():
    if j>=170:
        b[i]=j
print("Marks greater than 170:")
print(b)
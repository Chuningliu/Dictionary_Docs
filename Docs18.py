# Q18.Write a Python program to get the maximum and minimum value in a dictionary.
f={1: 2, 3: 0, 4: 3, 2: 9, 0: 7}
for i in f:
    a= min(f.values())
    b=max(f.values())
    if f[i]==a:
        a=f[i]
    elif f[i]==b:
        b=f[i]
print("Minimum value is",a) 
print("Maximum value is",b)
        
        
  

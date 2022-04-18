# Q21.Write a Python program to print all unique values in a dictionary. 
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
b=[]
for i in a:
    for j in i.values():
        if  j not in b:
            b.append(j)
print("Unique values are: ")
print(set(b))

   




        































# a= {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
# b=[] 
# for val in a.values(): 
#   if val in b: 
#     continue 
#   else:
#     b.append(val)

# print (b)


    
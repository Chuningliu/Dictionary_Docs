#  REMOVE UNIQUE VALUES
# Output:['Vishnu', 'Ram', 'sita']


a= {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
b=[] 
for val in a.values(): 
  if val in b: 
    continue 
  else:
    b.append(val)

print (b)

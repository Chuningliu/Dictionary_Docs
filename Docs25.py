# Q24.Write a Python program to combine values in python list of dictionaries. 
# Expected Output: Counter({'item1': 1150, 'item2': 300})


a= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
b={}
i=0
sum=0
while i<len(a):
   sum=sum+(a[i]['amount'])
   b['item1']=sum
   b['item2']=a[1]['amount']
   i=i+2
print("counter",b)





































# d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d1={}
# i=0
# c=[]
# while i<len(d):
# # while i<len(d):
#     if d[0][0]==d[i][0]:
#         a=d[i]
#         c.append(a[1])
#         d1[a[0]]=c
#     i+=1
# print(d1)
# output => Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

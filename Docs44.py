# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.

# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
c={}
d=[]
e={}
for i,j in a.items():
    for i in range(2):
        c["Science"]=a["Science"][i]
        e['Language']=a['Language'][i]
        b.append(c)
        d.append(e)
print(b,d)
        
    
# a={"science": [88, 89, 62, 95], "language": [77, 78, 84, 80]}
# length=len(a["science"])
# length1=len(a["language"])
# i=0
# dic={}
# list=[]
# while i<length:
#     dic["science"]=a["science"][i]
#     dic["language"]=a["language"][i]
#     list.append(dic)
#     i=i+1
#     print(dic)
    
    
    
 
# l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {}
# for i in l:
#     if i[0] in d:
#        d[i[0]].append(i[1])
#     elif i[0] not in d:
#            d.update({i[0]:[i[1]]})
# print(d)




dict={1:10,2:60,3:30,5:50,4:60,5:3}
output={10: [1], 60: [2, 4], 30: [3], 3: [5]}

i=1
a={}
c=[]
while i<=len(dict):
    a[dict[i]]=[i]
    a[dict[2]]=c
    j=i+1
    while j<len(dict):
        if dict[i]==dict[j]:
            c.append(i)
            c.append(j)
            a[dict[2]]=c
        
        j=j+1
    i=i+1
print(a)





# i=1
# a={}
# while i<len(dict):
#     a[dict[i]]=[i]
#     if a[dict[i]]==60:
#         a[dict[i]]=[i,i]
#     i=i+1
# print(a)
    
    
    
    
    
    

# print(dict[1])

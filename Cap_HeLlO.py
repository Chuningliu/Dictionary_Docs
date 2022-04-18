def capital_indexes(a):
    b=[]
    for i in range(len(a)):
        if a[i].isupper()==True:
            b.append(i)
    return b
print(capital_indexes("HeLlO"))


# def capital_indexes(a):
#     b=[]
#     i=0
#     while i<len(a):
#         if a[i].isupper()==True:
#             b.append(i)
#         i+=1
#     return b
# print(capital_indexes("HeLlO"))




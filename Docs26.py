# Q26.Write a Python program to print a dictionary in table format.
# Sample Output:
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

a= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print("C1","C2", "C3" )
# for i in a:
#     print(a[i])
#     print()
print("{:<10} {:<10} {:<10}".format('C1', 'C2', 'C3'))
for key, value in a.items():
    C1, C2, C3= value
    print("{:<10} {:<10} {:<10}".format(C1,C2,C3))
    
    

# for i in range(3):
#     for j in range (3):
#         print(a[i,j],end=" ")
#     print()

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # print(*row)



    
    


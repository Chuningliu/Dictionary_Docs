# Q33.Python: Print a dictionary line by line
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 
students={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}

for x,y in students.items():
    print(x)
    for i in y:
        print(i,":",y[i])
        




















# students={'Aex':{'class':'V'},'Puja':{'class':'V'}}
# a={}
# for i in students:
#         for j in students[i]:
#                 a[i]=j
# print(a)


               
        



# Q27.Write a Python program to count the values associated with key in a dictionary.
# Sample input if key is id: then 6




# a= [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# sum=0
# for i in a:

    
#     print(sum)

# b={}
# i=0
# sum=0
# while i<len(a):
#    sum=sum+(a[i]['amount'])
#    b['item1']=sum
#    b['item2']=a[1]['amount']
#    i=i+2
# print("counter",b)
        
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))







    














    
       
        
     
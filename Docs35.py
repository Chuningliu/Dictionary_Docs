# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# Sample output: 5
a=  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in a:
        for j in a[i]:
                count+=1
print(count)








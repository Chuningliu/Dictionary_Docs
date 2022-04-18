# Q40. Write a Python program to convert more than one list to nested dictionary. 
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
# a=['S001', 'S002', 'S003', 'S004']['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'][85, 98, 89, 92]

def nested_dictionary(a,b,c):
     result = [{x: {y: z}} for (x, y, z) in zip(a,b,c)]
     return result
id = ["S001", "S002", "S003", "S004"] 
name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
grade = [85, 98, 89, 92]
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(id,name,grade))




    
    
    
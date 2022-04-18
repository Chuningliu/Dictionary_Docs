# Q16.Write a Python program to map two lists into a dictionary.
students = ['Smith', 'John', 'Priska', 'Abhi']
marks = [89, 53, 92, 86]
for i in students:
    a= dict(zip(students, marks))
print(a)
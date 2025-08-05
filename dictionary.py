'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''
'''
1)Create an empty dictionary called bird

'''
bird={}

'''
2)Add name, color, breed, legs, age to the bird dictionary

'''

bird={'name':'pigeon','color':'black','breed':'white','legs':4,'age':'33'}
print(bird)

'''
3)Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
'''
student={'first_name':'jayaraj','last_name':'kanala','gender':'male','age':33,'marital_status':'single','skills':['python'],'country':'india','city':'banglore','address':'kota,andhrapradesh'}
print(student)
'''
4)Get the length of the student dictionary
'''

print(len(student))
'''
5)Get the value of skills and check the data type, it should be a list

'''
print(student['skills'])
print(type(student['skills']))

'''
6)Modify the skills values by adding one or two skills

'''
student['skills'].append('c++')
student['skills'].append('embedded systems')
print(student['skills'])

'''
7)Get the dictionary keys as a list
'''

print(student.keys())

'''
8)Get the dictionary values as a list

'''

print(student.values())

'''
9)Change the dictionary to a list of tuples using items() method
'''

print(student.items())
print(list(student.items()))

'''
10)Delete one of the items in the dictionary

'''
print(student.pop('gender'))

print(student)

'''
11)Delete one of the dictionaries

'''
del student






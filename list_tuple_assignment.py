'''
Q1) Create list called "even", store all the even numbers, in the range of 1 to 20.
'''
even=list()
for i in range(20):
    if(i%2==0):
        even.append(i)
print(even)
'''
Q2)Create list called "odd", store all the odd numbers, int the range of 1,20.
'''
odd=list()
for i in range(1,20,2):
    odd.append(i)
print(odd) 
'''
Q3)Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.
'''
numbers =even+odd
numbers.sort()
print(numbers)
'''
Q4)Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].
'''
'''student=list()'''

student=[["raj",1,20],["jaya",2,30],["raju",3,40],["harish",4,50],["rakesh",5,60]]
print(student)


'''Q5)Write a Python program to find the second largest number in a list.'''
arr=[5,1,10,30,2,4,8,9,11,12]
arr.sort()
print(arr[-2])

'''
Q6) WAP to print unique element from list.
     ex... nums = [4,3,5,6,3,4,6]      (o/p:- 5 is unique from list)
'''

arr=[4,3,5,6,3,4,6]

for x in arr:
    if arr.count(x)==1:
        print(x)

'''        
Q7)Given a tuple of numbers, find the max and min elements.
  ex.. tup = (11,26,45,23,15,18)
'''
tup = (11,26,45,23,15,18)
li=list(tup)
li.sort()
print(li)
print(li[0])
print(li[5])
'''
Q8) Retrieve the 'G' from following list using positive indexing
       L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
        
''' 
L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]

print(L1[3][2][2][1][1])
'''

Q9) WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
       L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
'''
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

'''
Q10) WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
      s2 = 'Hello I am going to Bengaluru How are you doing?'
'''
s2 = 'Hello I am going to Bengaluru How are you doing?'


reversed_city = s2[-20:-30:-1]
print(reversed_city) 







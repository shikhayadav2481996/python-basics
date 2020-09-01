# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:29:47 2020

@author: sakshi
"""
# CHAPTER 7 [ program contuct]
#----------------------------------

# if / else / if-elseif-else
# operators : relational , logical
# loops

# programming contruct

# checkif the given score is more than 10 
# if yes it is good quality
# else not a good quality

# if condition
score = 7 
if(score > 10):
    print("the quality is good")

####

# if condition
score = 14 
if(score > 10):
    print("the quality is good")

# else if condition
score = 7 
if(score > 10):
    print("the quality is good")
else:
    print("the quality is bad")


# ASSIGNMENT
# check if a number is divisible by 8 
# if yes print message number divisible by 8
# if no print message number not divisible by 8

number = 88
if(number // 8 == 0):
    print(number,'is divisible by 8')
else:
    print(number,'is not divisible by 8')


####
score = 10
# greater than or equal to
if(score>=10):
    print('the quality is good')
else:
    print('the quality is bad')
        
####
score = 3
# less than or equal to
if(score < 10):
    print('the quality is bad')
else:
    print('the quality is good')


# score more than 10 and status = 'green'
score = 12; status = 'green'

# multiple conditions
# AND ( 2 oor more conditions : all should be staisified)

if((score > 10) & (status == 'green')): # conditions we have to check before equality ==> Blank spaces and cases
    print('good quality')    
else:
    print('bad quality')
    
####
if((score > 30) & (status == 'green')): # conditions we have to check before equality ==> Blank spaces and cases
    print('good quality')    
else:
    print('bad quality')
    
    
# OR (any 1 condition to be true )
# either the score more than 10 or status has to be green
  

# score more than 10 and status = 'green'
score = 12; status = 'green'

if((score > 10) | (status == 'green')):
    print('good quality')
else:
    print('bad quality')


# NOT condition
# reject the item if status is not green

if(status != 'green'):
    print('item rejected')
else:
    print('item selected')

####
status = 'red'
if(status != 'green'):
    print('item rejected')
else:
    print('item selected')

# to check a number in range or not
# score is in a range between 4 and 5 then i have to mark it as 5* 

score = 4

# 1) method 
if((score >= 4) & (score <= 6)):
    print('score is in range')
else:   
    print('score out of range')

# 2) method 
if(score in range (4, 7)): # why we have use (4,7) => because in python 4 is included but 7 is not it is always taken as 7-1 = 6 that is 6   [range(4,7) gives 4 to 6 ]
    print('score is in range')
else:   
    print('score out of range')


# Assignment
# classify day as 'very hot' or 'hot' based on temperature
# if temp is <= 40.5, it is hot
# if temp is > 40.5, it is very hot

temp = 45.5
if(temp <= 40.5):
    print('it is hot')
elif(temp > 40.5):
    print('it is very hot')
else:
    print('it is not hot')


# else if condition
marks = 57
'''
'excellent', 'very good', 'good', 'average', 'needs imp'
95-100        85-94        70-84   50-69      <50
'''
if(marks in range(95, 101)):
    rank = 'excellent'

elif(marks in range(85, 95)):
    rank = 'very good'

elif(marks in range(70, 85)):
    rank = 'very good'

elif(marks in range(50, 70)):
    rank = 'very good'

else:
    rank = 'need improvement'
print('mark = {}, rank = {}'.format(marks, rank))


# if the marks entered is more than 100, rank = 'excellent' 
# should not accept negative marks

# mitesh
marks =255

if(marks >= 0):
    print("Enter positive number")
else:
    if (marks in range(95,101) | (marks>100)):
        print("Excellent")
    elif (marks in range(85,95)):
        print("Very Good")
    elif (marks in range(70,85)):
        print("Very Good")
    elif (marks in range(50,70)):
        print("Very Good")
    else:
        print("Needs Improvement")
       

# anand
if (marks >= 95):
    rank = 'Excellent'    
elif marks in range(85,95):
    rank = 'Very good'
elif marks in range(70,85):
    rank = 'Good'
elif marks in range(50,70):
    rank = 'Average'
elif marks in range(0,50):
    rank='Needs improvement'
else:
    rank = 'Invalid marks'
    print('mark={},rank={}'.format(marks,rank))


# sir
    


###### loops
# for loop
# works on an iterative object (eg lists , dict , tuple, matrix, etc)
# 2 ways:
#1 method = get the element directly
#2 method = using the index, get the elemn=ent from that position

countries = ['india', 'united kingdom', 'united states', 'ireland', 'indonesia', 'sri lanka']

#1 method = get the element directly
for e in countries:
    print('country = ', e)

#2 method = using the index , get the element from that position
for e in range(0, len(countries)):
    print('country = ', countries[e])


# while loop
num1 = 10
while(num1 > 1):
    print('number = ',num1)
    num1 -= 1

# i want to print the 1st 10 numbers starting from 1
# 1 2 3 4 5 6 7 8 9 10
num2 = 1
while(num2 < 11):
    print('number = ',num1)
    num2 -= 1
     
    
# if we want to break this loop in between then 
num1 = 10
while(num1 > 1):
    print('number = ',num1)
    num1 -= 1  
    if(num1 > 5):
        print('terminating loop after {}iterations'.format(num1))
        break
    
# break or terminating the loop after 6 iteration
num1 = 1
while(num1 > 1):
    print('number = ',num1)
    num1 += 1 
    #terminate the loop half way
    if(num1 > 5):
        print('terminating loop at the {} iterations'.format(num1))
        break
    
####
num1 = 1
while(num1 < 10):
    print('number = ',num1)
    num1 += 1 
    #terminate the loop half way
    if(num1 == 5):
        print('terminating loop at the {} iterations'.format(num1))
        break
    
    
# write 
n = 1
marks = int(input('enter number :'))    
while(n==1):
    if((marks < 0) | (marks > 100)):
        print('please enter number')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
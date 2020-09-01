# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:30:22 2020

@author: sakshi
"""

## chapter = 4  [ TUPLE ]
#  ----------------------------

# tuple is a record so every record is called a tuple so we can say list of record is called tuple
# immutable object (cannot change or unchangeable)
# ()
# tuple is also a iterable object

# homogeneouse data
lang = ('hindi', 'english', 'tamil', 'malayalam', 'bengali')
print(lang)
type(lang)
len(lang)

l = lang[0]
print(l)
type(l)

# access tuple
lang[0]
lang[0:4]
lang[-1] # last value

# concatenate a tuple
others = ('assamese', 'konkani', 'marathi')
lang = lang + others
print(lang)
len(lang)

# Assignment
# change the name of the element to convert the first character to upper case

lang[0] = lang[0].title() # tuple values cannot be changed directly because they are immutable

# to still change values
#1) step1 - convert the tuple to list

lang = list(lang)
print(lang)
type(lang)

#2) step2 - make changes
lang[0] = lang[0].title()
print(lang)

#3) step3 - convert list to tuple

lang = tuple(lang)
print(lang)
type(lang)

# print all element from 0 to last -1
lang[0:-1]

# delete a tuple so we cannot do it directly because tuple is immutable so we have to repeat above process
lang[4]
del lang[4] # error

# deletes the complete tuple along withthe contents and structure
del lang

# packing and unpaacking tuple ( heterogenous data )
# packing data
cric = ('abc', 31, 378, 10921, 45.67, True)
print(cric)

# unpacking data
name = cric[0]
print(name)

name, age, matches, runs, average, active = cric
print(name)
print(age)
print(matches)
print(runs)
print(average)
print(active)

# tuple

lang = ('hindi', 'english', 'tamil', 'malayalam', 'bengali')
others = ('assamese', 'konkani', 'marathi')
lang = lang + others
print(lang)

# check if a value exists in a given tuple
'french' in lang
'marathi' in lang

# get the index position of an element in a tuple 
lang.index('marathi')

# Assignment
# creat a tuple of words
# join the words to form a sentence
# ans =   " ".join(words)
t6 = ('mary', 'had', 'a', 'little', 'lamb')
word = ' '.join(t6)
print(word)
type(word)
type(t6)

# nested tuple
# roll, name, gender, age, educ, gpa, curr_trg

student = (
        (19, 'sriram', 'M', 20, 'B.Tech',4.17, 'MLP'),
        (45, 'priya', 'F', 19, 'BE', 4.51, 'PGDD'),
        (104, 'anu', 20, 'B.Com', 4.03, 'CIBOP'),
        (287, 'chiku', 'M', 23, 'PG', 3.87, 'Fashion')        
        )

print(student)

# access indidvidual tuples of a nested tuple
student[0]
student[3]

# extract GPA of the first student  
student[0][5]# this is how can drill down and get details

# get the curr training program of the second student
student[1][6]

# i want only 3 character of the curr trg program of a student
student[3][6][0:3]

# to bind all the columns of a nested tuples
all_data = tuple(zip(*student))
all_data[0]
all_data[1]

# Assignment
# create a tuple of grocery items (10 rows(items))
# columns
# itemname qty price total_price

#i) total_price = qty*price (to be calculated) 
#2) calculated  the grand total (total bill amount)
#3) identify the costliest and the cheapest item (based on the total_price)



items = ('milk','cold drink','butter','wheat','rice','bread','biscuit','maggie','sugar','jaggery')
items
qty = (1,2,4,2,1,4,6,7,2,3)
type(qty)
price = (25,15,10,50,60,10,20,10,30,70)
price[1]
total_price = []
pos = 0
# i)
for i in range(0,(len(qty))):
    total_price.append(qty[i]*price[i])
      
total_price = tuple(total_price)
total_price

# table

type(total_price)
table = (items , qty, price, total_price)
tables1 = tuple(zip(*table))
tables1

# ii) 
Grand_Total = sum(total_price)
Grand_Total

# iii) 
costliest = max(table[3])
ndx_costliest = total_price.index(costliest)
print("Costliest Item is",table[0][ndx_costliest])

cheapest = min(table[3])
ndx_cheapest = total_price.index(cheapest)
print("Cheapest Item is",table[0][ndx_cheapest])

# or




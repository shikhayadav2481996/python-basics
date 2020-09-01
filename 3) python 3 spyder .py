# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:35:02 2020

@author: sakshi
"""
city = ['mysore', 'mysore', 'pune', 'chennai', 'mumbai', 'bina', 'nagpur', 'kolkata', 'bangalore', 'kota', 'gwalior', 'jammu', 'kashmir', 'delhi']

# acces the list
city[::2] # city[0:len(city):2]

# starting from the 2nd element get every 3rd city
city[1::3]
print(city)

# how to change element of a list ( and that is known as mutation or mutable)
# list are mutable( means we cn change the values in the list)

#1 way
city[2] = city[2].title()
print(city)

#2 way
# instead of hard coding the index value get the index value first
ndx = city.index("mumbai")
city[ndx] = city[ndx].title()
print(city)

# delete an element from a list
city.append('a')
city.append('b')
print(city) # horizontal answer
city # vertical answer


#1 way
del city[city.index('a')]
print(city)

#2 way
city.remove('b')
print(city)

city.remove(["a","b"]) # so we cannot give or remove multiple value we have to remove element one by one
print(city)

# list is also called iterable object ( means we can iterarte element directly)

# accessing the individual element of a list
#1) get access to the element / value directly

for i in city:
    print('city = ',i)

# Assignment 
# using loop, change all the name of the cities to title case

for i in city:
    print(i.capitalize())

# or

for i in range(len(city)):
    city[i] = city[i].title()
    print(city)

# or
    
for e in city:
    city[city.index(e)]=city[city.index(e)].title()
print(city)

#2) get access to the element using the index 

for e in range(0,len(city)):
    print("city = ", city[e])


# creating a list with heterogenous data

# title, name, age, gender, height, weight, married

rec1 = ['Mr', 'Rajesh Kumar', 31, 'm', 175, 59.5, True]
print(rec1)

# if we want to extract values 
rec1[1]
rec1[3]

# unpacking records
salutation, name, age, gender, height, weight, married = rec1
print(salutation)
print(name)
print(age)
print(gender)
print(height)
print(weight)
print(married)


# how to make a copy of a list and do changes without affecting the original list
# shallow copy

rec1_copy = rec1
print(rec1_copy)

print(rec1)

# suppose we change copyed list
rec1_copy[2] = 36
rec1_copy[5] = 79.5
print(rec1_copy)

print(rec1)# so here we can see any change we have done in copyed list is getting reflected in the original list so we have to get rid of this 

# Assignment
# proper copy using the copy()
# deep copy

rec1_copy = rec1.copy()
print(rec1_copy)

print(rec1)

# suppose we change copyed list
rec1_copy[0] = 'Ms'
rec1_copy[1] = 'Seema Kumar'
rec1_copy[3] = 'F'

print(rec1_copy) # so now we can see the changes we have done in copyed list is not get reflected in the original list and this is done with the help of  [ copy() ]

print(rec1)

# creating a list
# link columns of different lists to form a record ( zip() ) so this zip is used
# answer = [('A', 5), ('B', 1), ('C', 9)]
# so this how we can make record using different list

name = ['A', 'B', 'C']
rank = [5, 1, 9]
list(zip(name, rank))


# nested list  = inside the -------------- list we have another lists (or we can say inside the list the element are list only)

num1 = [
        list(range(1,31,3)),
        list(range(1,31,7)),
        list(range(1,31,10))
        ]

print(num1)
len(num1)

# if we want to extract values from the list
num1[0]
num1[1]
num1[2]

# Assignment
# create a nested list to store the tables (2-10)
# format : 2,4,6,8,......,20
#          3,6,9,.......,30
#      ...............
#      ...........
#      10,20,30,.......,100
# no hardcoding
# answers (me)
num2 = [
        list(range(2,21,2)),
        list(range(3,31,3)),
        list(range(4,41,4)),
        list(range(5,51,5)),
        list(range(6,61,6)),
        list(range(7,71,7)),
        list(range(8,81,8)),
        list(range(9,91,9)),
        list(range(10,101,10))
        ]
print(num2)

# or jai

store = [2,3,4,5,6,7,8,9,10]
multip = [1,2,3,4,5,6,7,8,9,10]
for i in store:
    for j in multip:
        print(i*j)

# or sahil
tables = []     
for e in range(2,12):
    for i in range(1,e):
        tables=[list(range(i,i*11,i))]
        print(tables)

# or sir

tables1 = []
for i in range(2,11):
    tables1.append(list(range(i,(i*10)+1,i)))
    print(tables1)

# or mitesh
n = 10
table = [['1']*(n+1)for _ in range(n+1)]# here he is initialising table
for i in range(1,n+1):
    table[i][0] = i
    for j in range(1,n+1):
        table[0][j]=j
        table[i][j]=i*j
table


# from the 3rd element of the list get the first five element
tables1[2]
tables1[2][0:5]

sum(tables1[2][0:5]) # for finding sum
sum(tables1[2][0:5])/5 # for finding average 
max(tables1[5][0:6]) # this how we cn find maximum values

# find if an element exists in the list ( or how can we find existance of the element in the list)

'bhopal' in city
'kashmir' in city

# nested list with characters

maps = [
        ['india','uk','us','indonesia'], ['delhi','london','washington dc','jakarta'], ['rupee','pound','dollar','rupiyah']
        ]

print(maps)
countries = maps[0] # if we want to extract values from the list
print(countries)

# if we want to extract values from the list
maps[1]
maps[2]

# Assignment
# 1) using the city list , print the name and length of the city.
# expected output : city = pune, length = 4



# 2) using the maps, print the 
# expected output : country, capital, currency ( don't use the zip() function)

# example =  india, delhi, rupee( expected format )
maps = [
        ['india','uk','us','indonesia'], ['delhi','london','washington dc','jakarta'], ['rupee','pound','dollar','rupiyah']
        ]

list = [[row[i] for row in maps] for i in range(4)]
print(list)


# or ajinkya

for i in range(0,3):
    print('\n')
    for j in maps:
        print([j[i]], end = " ")


# or ananad

for i in range(len(maps[i])):
    if i==0:print(maps[i][i],maps[1+i][i],maps[i+2][i])
    elif i==1:print(maps[i][i],maps[1+i][i],maps[i+2][i])




# or mitesh
a = maps[0] 
b = maps[1]
c = maps[2]
merged_list = [(a[i], b[i], c[i]) for i in range(0, len(a))]
merged_list


# tanmay
res1 = [i[0]for i in maps]
res2 = [i[1]for i in maps]
res3 = [i[2]for i in maps]
res4 = [i[3]for i in maps]
print("Final List:\n",res1, "\n" ,res2, "\n" ,res3, "\n" ,res4)

# aishwarya
for i in range(4):
    print("\n")
    for j in maps:
        print(j[i],end = " ")


# NESTED list generation

length = []; width = []; height = []

import random as r
for i in range(20):
    length.append(round(r.uniform(20,40),2))
    width.append(round(r.uniform(10,15),2))
    height.append(round(r.uniform(2,6),2))
table = [length, width, height]
print(table)

# extracting list element using indexing 
table[0] 
table[1]
table[2]












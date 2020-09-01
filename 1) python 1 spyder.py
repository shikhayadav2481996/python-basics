# -*- coding: utf-8 -*-
"""
Spyder Editor           # multiline comments
date = 28-4-2020 
This is a temporary script file.
"""
# topics in python to be covered
#---------------------------------

# ch1 = variable and numbers 
# ch2 = strings
# ch3 = lists
# ch4 = tuple
# ch5 = dictionary
# ch6 = sets
# ch8 = if_else / loops
# ch9 = functions / lambda function

# specialized python libraries
# ch10 = numpy
# ch11 = pandas(dataframes)
# ch12 = visualization
# ch13 = EDA
# ch14 = oops ( object oriented programming techniques)
# ch15 = scikit learn( machine learning)


#########################################
# select line and press ctrl+enter

# or keep curser at the starting point of line then click on console k niche jo icon h

# if want to clear console then prees ctrl + l

# if we click on run k niche wala icon it will run whole file


#############################################

# ch 1 = number and variables
#-----------------------------

# number sequence
list(range(10))
#  or
print(list(range(10)))

# numbers from 1-10
list(range(1,11))
#  or
print(list(range(1,11)))

# start from 1 and end at 11-1

# range of numbers with a given interval
# starting from 1, end at 30 and print every 4th number
print(list(range(1,31,4))) # this how we can give step size

# range of numbers in the reverse order
print(list(range(10,0,-1))) # reverse 

# random numbers
# how to import libraries
import os

# how to get the function names from a library
dir(os)

os.getcwd() # name of the library and then (.) & then function name

# this is how we can take help
help(os.listdir)
os.listdir()

# how to generate random numbers

import random as r # alise name
dir(r)

r.randint(10,50) # it will generate 1 random number

help(r.randint)

r.randint(1,5)# it will generate 1 random number

# to generate multiple random numbers

# use a for loop to generate multiple numbers

# in python there is no function to generate multiple random numbers so we use for loop 
# select both the lines and run

# generate random integers with replacement

for i in range(50):
    print(r.randint(10,100), end = " ") # these random numbers are generated with replacement 

# generate random integers without replacement

# i.e. unique values
    
r.sample(range(1,30),20) # sample size = 20, it take two input
r.randint(range(10,100),50)  ### it will not give the result because randint is used to get only one particular random number at a time, if we want to use this function for muiltiple random number then we have to use for loop for it and inside for loop we have to use this function ### 


# Assignment 

# generate 20 random 4 digit numbers ( with replacement)

for i in range(20):
    print(r.randint(1000,9999), end = " ")

# generate 20 random 4 digit numbers ( without replacement)
    
r.sample(range(1000,9999),20)


# to generate random float numbers
num1 = r.uniform(10,20) # it will generate one random number
print(num1)

# this is how we can check data type
type(num1)

num2 = round(num1,3) # it will give us the result till 3 digit after decimal because of round and 3
print(num2)

# or
num3 = round(r.uniform(10,20),3);print(num3)
##or
num3 = round(r.uniform(10,20),3) ## it will give same result ##
print(num3)


# Assignment

# generate day temperatures of 100 different districts in india . temperature range is [28 - 45], with a 1 decimal precision

# representation of large numbers
1e5 # 1 lac
1.2e2 # 120 ## how ?? ## 1.2 * 10^2(corresponds to 2) =120

1e5 + 1.2e2

# math library

import math
dir(math)

math.log()# library followed by function and log function take only one input

math.log(45)
round(math.log(45),2)

math.pi
math.e

num1 = 35; num2 = 22
num1+num2
num1-num2
num1/num2
num1*num2

# if want to find REMAINDER
num1%num2

# power
pow(5,3) # 5*5*5


# returns the integer portion
num1 = 13.566

math.floor(num1)
int(num1)

# next higher number of the in teger part 
math.ceil(num1)

# Assignment 

# pi * r square * h
# return the answer with 2 decimal places precision
radius = r.uniform(3,8)
h = r.uniform(10,15)
round(math.pi*pow(radius,2)*h,2)


##################################################

#  ch2 = STRINGS
#---------------------

str1 = 'c'
str2 = 'apple'
srt3 = "C"
str4 = "apple"

type(str1)
type(str4)

# convert a string into characters
# using list()
list(str2)

# using the index position
str2[0]
str2[1]
str2[4]

# length of the string
len(str2)

# string processing
str5 = "python ia a programming language. i am learning python and is very easy. python is based on oops. python is also a type osf snake"

# length includes the spaces
len(str5)

# substring 
# extract the first 10 characters
c1 = str5[0:11] # it give us first 11 character
len(c1)
print(c1)

# string concatenation (+ operator)

random1 = str5[0:5] + str5[15:20] + str5[50:60]
print(random1)
type(random1)

# we can not add character and a number
# so how can we add or append a number to a string
# first convert the number into a string format as we have done below  
random1 + str(12345)
# or
random1 + "12345"

# static string vs dynamic string

# STATIC STRING = which we initialize before running, example->str1="python"
# information does not change example -> week days

# DYNAMIC STRING =information get changeing eample -> temperature

msg1 = "there are 7 days in a week"
print(msg1)

boys = 30; girls = 45

print("total students present today = {},\n boys = {},\n girls ={}".format(boys+girls, boys, girls)) # \n = new line

# Assignment

# expexted output ( using for loop) 
# <> liter = <> ml
# erpected answer
"""
2 = 2000
1.5 = 1500
3 = 3000
do this for 10 random integers use a for loop
"""
# random numbers
# how to import libraries
import os

# ho wto get the function names from a library
dir(os)

import random as r # alise name
dir(r)

for i in range(10):
    liter = r.randint(1,100)
    ml = liter*1000
    print("liter ={} ml= {}".format(liter,ml))

# or 

for i in range (10):
    lit = round(r.uniform(2,10),2)
    mlit = lit*1000
    print("lit = {}, mlit = {}".format(lit,mlit))
    print("end of iteration",i)
    print("-------")

# repeating a word 
"apple"*3   # opperator overload
['pune']*3










# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:30:07 2020

@author: sakshi
"""

# nested dictionary
customer = {} # empty dictionary
customer['custid'] = 377899391 #1st key value 
customer['name'] = {'frame' : 'rajesh', 'middle' : 'pk', 'iname' : 'kumar'} # nested dictionary

customer['gender'] = 'M'
customer['age'] = 40
customer['address'] = {'a1' : '162 lake gardens', 'a2' : 'hadapsar', 'city' : 'pune', 'state' : 'MH', 'pincode' : 40001, 'landmark' : 'near abc pharma'} # we have parent dictionary in that we have sub dictionarys that is known as nested dictionary

print(customer) # nested dictionary

# access a nested dictionary

customer['custid']
# city name
customer['address']['city'] # dictionary ==> parent key ==> child key
# last name of the custommer
customer['name']['lname']  # dictionary ==> parent key ==> child key


# get all the nested keys
# all the high level keys
customer.keys()

# keys for the selected key
customer['name'].keys() 

# value for a selected key
customer['name'].values()

# name value pair as a tuple ; for a selected key 
customer['name'].items()

# Assignment

# create a nested dictionary to create service related information (services that are running in your pc)
# take a max of 10 services
# the status of the services should have both ' Running ' and ' Stopped '

services = {}
services[1] = {'pid' : 0, 'name' : 'ClipSVC', 'desc' : 'client license service', 'status' : 'stopped', 'group' : 'wsappx'}

services[2] = {'pid' : 4828, 'name' : 'sppsvc', 'desc' : 'software protection' , 'status' : 'running', 'group' : ''}
print(services)

# access the dictionary
services[1]['status']
services[2]['status']

###########################################################################

# CHAPTER 6  [ Sets 'STATUS' ]
#---------------------------------

# what is a set? 
# set is the unique collection of data or Every data point is unique
# set is collection of items so it will take list of values
# {}
# set has only values

# these are three things mainly we do on stes a) union, b) intersection, c) difference ==> i) a-b,  ii) b-a,  iii) symmetric difference


# creating set
a = set([19, 13, 7, 1, 23, 45])
print(a)
type(a)
len(a)

# sets are a unique collection of similar items
b = set([2, 18, 14, 12, 6, 6, 8, 8, 22, 46, 18, 18, 18])
print(b)
type(b) 


# Assignment
# create 2 sets of colors
# ensure that a few colors in set1 are in set2
# and a few colors of set2 are in set1

set1 = set(['red', 'green', 'blue', 'black', 'white']) # creating set
set2 = {'yellow', 'green', 'white', 'orange', 'indigo', 'violet'} # creating set
type(set1)
type(set2)

# convert a sentence into a bag of unique words
sent1 = 'ice is frozen water. ice is cold. ice is not good to consume. there is ice in my freezer.' # now we want unique element or words in this sentance 

# so for converting above sentance into bag of words we use split function
# and for unique words we use set because set have unique values or element 
bag_of_words = set(sent1.split())
print(bag_of_words)

# union [ A  UNION  B ]
c = a.union(b)
print(c)

z = set1.union(set2)
print(z)

z = set2.union(set1) # we will get the same result
print(z)


# intersection ( common element in both the sets )
common = set1.intersection(set2)
print(common)
type(common)


common = set2.intersection(set1)# we will get same result
print(common)
type(common)

# difference
# A - B [ all element of A not in B ]
s = set1.difference(set2)
print(s)

r = set1 - set2
print(r)

# B - A [ all element of B not in A ]
x = set2.difference(set1)
print(x)

v = set2 - set1
print(v)

# symmetric difference ( all the values from A Nd B except the common values )

# element are present in any 1 set, but not in both 
m = set1.symmetric_difference(set2)
print(m)

# converting a list with duplicated values into a unique collection of values
names = ['set', 'scale', 'scale', 'book', 'set', 'light', 'number', 'scale', 'light']
names.sort() # here we are sorting list
names

names = list(set(names)) # here converting list into set and then again converting it into list
print(names)
type(names)

##############################################################################

# CHAPTER = 8 [ DATES ]
#--------------------------


import datetime

# get the current date
today1 = datetime.datetime.today()
print(today1)

today2 = datetime.datetime.now()
print(today2)

print('{} {}'.format(datetime.datetime.today(), datetime.datetime.now()))

# the output is of the format  yyyy - mm - dd  hh24 : mi : ss : ms
print(today1)

# get the different components of the data time
today1.year
today1.month
today1.day
today1.hour
today1.minute
today1.second
today1.microsecond

# convert the date into dd/mm/yyyy format
datetime.date.strftime(today1, "%d/%m/%y")

# convert the date into dd/mm/yyyy hh24 : mi : ss format
datetime.date.strftime(today1, "%d/%m/%y %H:%M:%S") # captal H ;M ;S

# convert date into a 12 hour format
# %I --> 12 hour format

datetime.date.strftime(today1, "%d/%M/%y %I:%M:%S")

# get a previous time
# day(s) difference
prev = today1-datetime.timedelta(days = 1)
print('today = {}, \nprev = {}'.format(today1,prev))

# minutes difference
prev = today1-datetime.timedelta(minutes = 40)
print('today = {}, \nprev = {}'.format(today1,prev))

# seconds difference
prev = today1-datetime.timedelta(seconds = 200)
print('today = {}, \nprev = {}'.format(today1,prev))


# HELP
help(datetime.timedelta)


# years difference
prev = today1-datetime.timedelta(weeks = 104)
print('today = {}, \nprev = {}'.format(today1,prev))


# get a future date/ time
future = today1+datetime.timedelta(days = 1) 
print('today = {}, \nnext = {}'.format(today1,future))


# years difference

prev = today1-datetime.timedelta(weeks = 104)
print('today = {}, \nnext = {}'.format(today1,future))

# difference between 2 dates
# this gives the difference in days
today = datetime.datetime.today()
today

bday = datetime.datetime(1999, 1, 1, 10, 45, 00)
bday

diff = today - bday
print(diff)


# to get the difference in years , use this library
from dateutil.relativedelta import relativedelta

relativedelta(today1, bday)

# difference between 2 date of birth

dob1 = datetime.datetime(2001, 9, 13, 11, 45, 00)
dob2 = datetime.datetime(2004, 11, 25, 16, 21, 15)
relativedelta(dob2, dob1)







# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:34:15 2020

@author: sakshi
"""


# chapter = 5   [ DICTIONARY ]
#-------------------------------



# dictionary = always have a key value pair 
# []
# key = age ex 40 age : 40, name : abcxd

channel = {} # empty dictionary
# channel id = key
# channel name = value

type(channel)
channel[600] = "learning channel"
channel[601] = "english news"
channel[602] = "hindi news"
channel[603] = "hindi movies"
channel[604] = "english movies"
channel[605] = "circket"
channel[606] = "soccer"
channel[607] = "cartoon"

len(channel)
print(channel)

# key are always unique
# key can be numeric \ character \ alphanumeric
channel["PN"] = "pune news channel"
channel["IC"] = "india cricket"

print(channel)
len(channel)

channel["EDU1"] = "science classes"
channel["EDU2"] = "accountancy"

print(channel)
len(channel)

# create a dictonary (num1) in the following format :
# a1)
# num1[key] = value
# key = 1 - 50
# value = square of the key

# 1:1, 2:4, 3:9, ..........
# no hardcoding

num1 = {}
for i in range(1,51):
    num1[i] = i*i

print(num1)

# how to access the dictionary
# we have to use key to get the value
# we can give only one key at a time we can not use multiple key at a time

channel[101]
channel[601]
channel[605]

# other methods to access dictionary
#1 by key = value pair
print(channel) # 1 method

print(channel.items()) # we will get values in th tuple format
for k,v in channel.items():
    print('key = {}, value = {}'.format(k,v))
 
#2 by keys only
channel.keys()

# check the presence of a key in the dictionary or not
# both 83 and 84 line do the same action i.e. it checks for the presence / absence of key 

'IND1' in channel.keys()# it returns true or false
606 in channel # thats the default action [ .keys() ] and when we are not using .keys() both are going to return keys only 

#3 by values only
channel.values()

# check if a values exists in the dictionary
'english' in channel.values()
'english news' in channel.values()

value = 'AccOuntaNCY'
value in channel.values()# we will get false because it is case sensitive

#  how to make this return true; since the word 'accountacy exists in the dictionary

value = value.lower()
value in channel.values()

# or

value.lower() in channel.values()


# how to merge dictionaries
d_full = dict(list(channel.items()) + list(num1.items()))
print(d_full.keys())

type(d_full)
print(d_full.values())

2500 in d_full.values()
5 in d_full # 5 is present as a key in the dictionary and by default it will take it as key only

# how to change values for a given key
print(channel['EDU1'])

channel['EDU1'] = 'maths'
channel['EDU1'] # or
print(channel['EDU1'])

# remove a key value pair
del channel['EDU1']

print(channel.keys())

# how to creat a dictionary with single key with multiple values
# creat a dictionary with key : multiple value

#1 productID  : alphanumeric(10)
#2 productName  : character
#3 Qty(quantity)  : integer(1000 to 200000)
#4 Rate : float(25 - 250) [ with 1 deciaml precision ]
#5 Instock ( Y / N ) : 
#6 reOrder level  : integer [10 - 30]
#7 visibility (0 - 1) : float [0-1] ;  lower no. means it is not getting solded and higher no. means it is getting solded

# no hardcoding

# example
'''prodid = []; prodname = []; qty = []; rate = []; instock = []; record = []; visib = []

import random as r
sno = list(range(1,51)) # serial number

print(sno, end = " ")'''

import random as r
import string as s

# empty list of each data
product_id = [];
product_name = [];
quantity = [];
rate = [];
instock = [];
reorder = [];
visibility = []

#list of serial number
sno = list(range(1,51))
print(sno, end = " ")

# list of quantity; rate; reorder; visibility

for i in range(50):
    quantity.append(r.randint(1000, 20000))
    rate.append(round(r.uniform(25,250),2))
    reorder.append(r.randint(10, 30))
    visibility.append(round(r.uniform(0, 1),2))
    
print(quantity, end = " ")
print(rate, end = " ")
print(reorder, end = " ")
print(visibility, end = " ")   
    
# list of  in stock
instock = ['Y'] * 29 + ['N'] * 21
instock = r.sample(instock,len(instock))
print(instock, end = " ")


letters = s.ascii_uppercase +s.ascii_lowercase
letters = r.sample(letters, len(letters))



# list of product id 
for i in range(50):
    p1 = r.randint(1000,9999)
    rnum = r.randint(1, len(letters) % len(letters))
    
print(product_id, end = " ")

# list of product name
for i in range(50):
    p2 = ''.join(letters[rnum:rnum+3])
    product_id.append(str(p1) + '/' + p2)
    
    product_name.append(p2)

print(product_name, end = " ")
    

letters = s.ascii_uppercase +s.ascii_lowercase
letters = r.sample(letters, len(letters))

import string as s 
for i in range(50):
    p1 = r.randint(1000,9999)
    rnum = r.randint(1, len(letters) % len(letters))
    p2 = ''.join(letters[rnum:rnum+3])
    product_id.append(str(p1) + '/' + p2)
    
    product_name.append(p2)
    
    quantity.append(r.randint(1000, 20000))
    rate.append(round(r.uniform(25,250),2))
    reorder.append(r.randint(10, 30))
    visibility.append(round(r.uniform(0, 1),2))
    

print(sno, end = " ")
print(product_id, end = " ")
print(product_name, end = " ")
print(quantity, end = " ")
print(rate, end = " ")
print(reorder, end = " ")
print(visibility, end = " ")     

# create the dictionary having kry with multiple values
d_inventory = {'sno' : sno, 'product_id' : product_id, 'product_name' : product_name,
               'quantity' : quantity, 'rate' : rate, 'instock' : instock, 'reorder' : reorder, 'visibility' : visibility}

print(d_inventory)

# access the dictinoray
d_inventory.keys()
d_inventory['product_id']
d_inventory.values()


#######################  or sir  ######################################

import random as r
import string as s

prodid=[]; prodname=[]; qty=[]; rate=[]; instock=[];
reord=[]; visib=[]

letters=s.ascii_uppercase + s.ascii_lowercase
letters=r.sample(letters,len(letters))

sno = list(range(1,51))

# in-stock
instock = ['Y']*29 + ['N']*21
instock = r.sample(instock,len(instock))


for i in range(50):
    p1 = r.randint(1000,9999)
    rnum = r.randint(1,len(letters))%len(letters)
    p2 = ''.join(letters[rnum:rnum+3])
    prodid.append(str(p1)+"/"+p2)
    
    prodname.append(p2)

    qty.append(r.randint(1000,20000))
    rate.append(round(r.uniform(25,250),2))
    reord.append(r.randint(10,30))
    visib.append(round(r.uniform(0,1),2))
    

print(sno, end=" ")
print(prodid, end=" ")
print(prodname, end=" ")
print(qty, end=" ")
print(rate, end=" ")
print(instock, end=" ")
print(reord, end=" ")
print(visib, end=" ")

# create the dictionary having key with multiple values

d_inventory = { 'sno':sno, 'product_id':prodid,
               'product_name':prodname,
               'qty':qty, 'rate':rate,
               'instock':instock,
               'reorder_level':reord,
               'item_visibility':visib  }
print(d_inventory)

# access the dictionary
d_inventory.keys()
d_inventory['product_id']
d_inventory.values()










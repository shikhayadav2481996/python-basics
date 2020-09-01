# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:34:55 2020

@author: sakshi
"""

# starting from the 1st character every "n" characters from a string

str3 = "python ia a programming language. i am learning python and is very easy. python is based on oops. python is also a type osf snake"

str3[::3] # it start from 0(zero)and the secand (:)colun is where i will end and the third colun(:) is the steps


# Assignment
# using a for loop how can the same operation be done? # 

for i in range(0, len(str3), 3):
    print(str3[i])
## or

length_str3 = len(str3)
for i in range(0, length_str3, 3):
    print(str3[i])


# find a string within a string 
word_to_find = 'python'

#1) check if the string exists

word_to_find in str3
'Language' in str3 # because python is case sensative 
"a" in str3

word_to_find in str3
'language' in str3 
'tho' in str3
'gram' in str3

#2) check the number of times  the string repeats
str3.count(word_to_find)
str3.count('c++')
str3.count("a")

# 3) get the index positions of every repeated occurance

# there are two function in python for gettting index position :-
#i) get the index position of the 1st occurance of the word
str3.find(word_to_find)

#ii) get the index position of the last occurance of the word
str3.rfind(word_to_find)

# check if a string starts with a particular character / string or not

str3.startswith("machine")
str3.startswith("p")
str3.startswith("word_to_find")

# count of vowels in str3
print("vowel count : \n A={},\nE = {},\nI = {},\nO = {},\nU = {}".format(str3.count('a')+str3.count('A'),str3.count('e')+str3.count('E'),str3.count('i')+str3.count('I'),str3.count('o')+str3.count('O'),str3.count('u')+str3.count('U')))

str3

# check is a string ends with a particular character
str3.endswith("r")
str3.endswith("ke")


# Assignment
# find the index position of all the words repeating in a sentence


# find and replace in strings 
# replace the "python"(small p) with "Python"(capital P)
# output on the console of old values are retained ( in this case old string will remain same )
str3.replace("python","Python")

print(str3) # when we are going to change something in th estring the main string will remain same the main string will not change

# old values or string are replace in the variable after assignment

str3 = str3.replace("python","Python")
print(str3)

# ocnvert strings / words to cases (upper/lower)
word1 = "program"
word1 = word1.upper()# convert full string in the upper case charater
print(word1)

word1 = word1.lower()# convert full string in the lower case charater
print(word1)

# converts the first character of a word into capital
word1 = word1.capitalize()
print(word1)

# convert all the first letter present in the string in the capital letter
print(str3)
str3.title()

# get the ASCII value of the character ( ASCII is the numerical representation of a charater )
ord('a')
ord('A')
ord('%')

# dealing with spaces in python
# there are mainly four type of white spaces #1) spacebar 1 white space front 
#2) backspce 1 white space back
#3) tab 7 white spaces( can be coustmaised into 5)
#4) enter key

# are these above spaces treated same = so they all are different

word1 = '   python    '# 3 spaces before character 4 spaces after charater
print(word1)
len(word1)

# remove spaces (of spacebar)
#1) spcaes from the left side of the string
w1 = word1.lstrip()
print(w1)
len(w1)

#2) spaces from the right side of the string
w2 = word1.rstrip()
print(w2)
print(len(w2))

#3) spaces from left and right side of the string
w3 = word1.strip()
print(w3)
print(len(w3))


sent1 = "    the movie Extraction was good. it has\t\t\t\t a nice story and \n\n\n\n\n a nice plot. good direction and    the casting \t\n\n was excellent \n\n\t "# tab is represented as \t and eter key is represented as \n
print(sent1)
sent1.strip()

# this is who we can get rid of all white spaces with the help of split and join function :-

#1) split the sentance into individual words

words = sent1.split() # splits at every white space ( default action)
print(words)
#2) combine the word into a sentence with a default " "

sent1 = " ".join(words)
print(sent1)


# split a record at other delimiters
rec1 = "PG10890~Rajesh~M~PG in ML~10/05/2020~1~BE(Chemical)"

# specify the delimiter
q = rec1.split("~")
print(q)
g = "".join(q)
print(g)

# specify the path name properly

path = "D:\new\term1\break\glass.csv"
print(path)

path = "D:\\new\\term1\\break\\glass.csv"
print(path)

path = "D:new/term1/break/glass.csv"
print(path)

# getting user input
name = input("enter a numbre :")
print(name)
type(name)

int(name)+10

str1 = "12345"
type(str1)
print(str1)
str1 + 200
# convert the string into numeric
# convert string to integer
int(str1)+200

# convert string to float
str = "123.25"
float(str1)+12.5

# this will not get converted
str1 = "fghafs"
int(str1)
float(str1)


##################################################################

# chapter = 3 [ LIST ]
#-----------------------


# list = is prefixed with the square bracket [ ] it can ahve all character it can ahve all numbers it is mutable

city = ["pune", "chennai", "mumbai", "kolkata", "bangalore"]
print(city)
type(city)

# how many number of element are there in the list

print(len(city))
# or 
len(city)

# how to access the list using the index position
city[0] # first value in the list
city[1] # secand value in the list
city[-1] # last value in the list

city[len(city)-1] # city name of index(-1)

# range of values ( printing first 3 cities)
city[0:3]

# every alternate city starting from the first value 
tier1 = city[::2] # slicing

print(tier1)

# how to add element to a list

# adding always at the end of the list
city.append('gwalior')
city.append('jammu')
city.append('kashmir')
city.append('delhi')

print(city)
len(city)

# how to add element in between two elements 

# add 'nagpur' in between mumbai and kolkata
# ....., mumbai, nagpur, kolkata,....

# 1 step = what is the index position of the city name
city.index('mumbai')
ndx = city.index('kolkata')
print(ndx)
city.insert(ndx,"nagpur")
print(city)

# or  how to add element in between two elements
# add 'kota' in between bangalore and gwalior 
# banglore, kota, gwalior
city.insert(city.index('bangalore')+1, 'kota')
print(city)

# add a new city "mysore" as the first city in the list

city.insert(0,'mysore') # this is more appropriate
print(city)
# or 

city.insert(city.index('pune'), 'mysore')
print(city)


# how to add element in between two elements 

# add 'bina' in between mumbai and nagpur
# ....., mumbai, bina, nagpur,....

city.index('mumbai')
ndx = city.index('nagpur')
print(ndx)
city.insert(ndx,"bina")
print(city)













































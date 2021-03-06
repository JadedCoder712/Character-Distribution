"""
distribution.py
Author: Kyle Postans
Credit: Kyle Postans, Mr. Dennison

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
"""What I want to do is make a list of uppercase and lowercase lists. 
Then make a thing that takes the list of upper/lowercase letters and creates a variable for each letter with the number of times it shows up. 
Then create a list of those variables (which have numbers of letters in the sentence attached to them). Sort them by amount. 
"""

sentence = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is: '.format(sentence))

import string
from operator import itemgetter, attrgetter, methodcaller

bignumber=len(sentence) #unnecessary
numbers=range(1, int(bignumber)) #unnecessary

sentencelist=list(sentence) #turns the sentence into a list of letters

megalist= string.ascii_lowercase #makes a list of lowercase letters

finallist=[]    #creates final list in order to put tuples into
 
sentence1=[x.lower() for x in sentencelist] #makes all letters lowercase


#The Actual Program:

#creating the list of tuples by putting each letter with the times they appear in the sentence:
for letter in megalist:
    number=sentence1.count(letter)
    if number is not int(0):
        variables=(number, letter)
        finallist.append(variables)
    

#sorting the tuple list into reverse alphabetical order, then leaving those properties in place while puttiing it order of appearance AND alphabetical order:

finallist1=sorted(finallist, key=itemgetter(0,1))

#finallist2=sorted(finallist1, key=itemgetter(0))

#finallistreversed=list(reversed(finallist1))

#print(finallistreversed)

finallistreversed = list(finallist1)

#creating the actual list of letters by multiplying the letters in the tuples by the amount of times they appear:
for x,c in finallistreversed:
        if x is not int(0):
            print(x*c)

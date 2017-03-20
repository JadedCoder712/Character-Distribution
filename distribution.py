"""
distribution.py
Author: Kyle Postans
Credit: Kyle Postans, Kyle Postans

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
'''
sentence = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is: '.format(sentence))
'''

import string

sentence= "CCCABBBBBEDD"
bignumber=len(sentence)
numbers=range(1, int(bignumber))

sentencelist=list(sentence)
megalist= string.ascii_lowercase

finallist=[]

sentence1=[x.lower() for x in sentencelist]



for letter in megalist:
    number=sentence1.count(letter)
    variables=(number, letter)
    finallist.append(variables)
finallist.sort()

for x,c in finallist:
    if x is not int(0):
        print(x*c)


    
    
    
    


        

        







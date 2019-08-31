from sys import argv
import re
import string
frequency  = {}
from collections import Counter
#makes a list called wrds
wrds = []
print("Hello wordCount")
#opens the txt file and reads
f= open(r"declaration.txt","r",encoding="utf-8-sig")
#makes a file called wordcountkey and reads and write
fout = open("wordcountkey.txt","w+")
#reads lines from declarations stored in varible f
for line in f.readlines():
    for word in line.split():
        #take out commas and periods to make things look kawaii desho
        word = re.sub(',','',word).replace('.','')
        wrds.append(word.lower())
wrds.sort()
count= Counter(wrds)


for item in count.items():

    fout.write("{}\t{}\n".format(*item))
f.close()







# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# Author: Ousmane Sow
# Program Function: Open txt files give word count of files and give top 30 words
# Top 30 words list code 
# function print_file_stats (location 5347)

import csv
import os

# User promt 
# fname = input('Enter file name: ')
# confirm file exists
# try:
  #  fhand = open(fname, 'r').read()
# error msg if not file exists
#except: 
  #  print('File cannot be opened:', fname)
    #exit()

#fname = open("/Users/ousmanesow/Desktop/RSP_Analysis/nihlong.txt", "r")
#try:
 #  fhand = open(fname, 'r').read()
# error msg if not file exists
#except: 
 #   print('File cannot be opened:', fname)
  #  exit()

#print (fhand)

 #desktop Path
desktopPath = '/Users/ousmanesow/Desktop/RSP_Analysis'

with open(os.path.join(desktopPath, 'nihlong.txt'), 'r') as f:
    
   # fhand = f.read()
    fhand = f.readlines()
    fhand = ' '.join(fhand)
    print(fhand)


# make everything lower characters 
fhand = fhand.lower()
# count characters
nchar = len(fhand)
print('Characters: ', nchar)
# count lines
#nlines = fhand.count('\n')
#print('Lines: ', nlines)
num_lines = fhand.count('\n')
print('Lines: ', num_lines)

# making a stop word list for more accurate analysis
stpwrdlst = [' the', ' to', ' are', ' from', ' or', ' and', 'we ', ' of', ' your', ' you', 'may ', ' our', ' this'
            , ' with', ' that', ' for', ' such', ' other', 'when', ' is', ' by', ' as', ' on', ' will', ' a', ' can',
             ' it', ' if ', ' be', 'in ', '*', 'who ', 'how ', 'more ', 'many ', 'not ', 'like ', 'have ', 'do ', 'which',
            'so ', '�']
# loop to remove stop words
for word in stpwrdlst:
    fhand = fhand.replace(word, '')
    

# my dictionary named d
d = dict()
words = fhand.split()
# for each word in dictionary, if it exists in dictionary, up count by one for that word 
for word in words: 
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

   # d[word] = d.get(word, 0) + 1
# computing the total numer of words  
nwords = sum(d[word] for word in d )
print('number of words (without stop words): ', nwords)

# dictionary for repositories
rname = {'dataverse': 0, 'dryad': 0, 'figshare': 0, 'mendeley data': 0, 'open science framework': 0, 'vivli': 0, 'zenodo':0, 'dash': 0, 'clinicalTrials': 0, 'xnat': 0}

# loop
for word in words:
#for word in list(d.keys()):
    if word in rname:
        rname[word] = rname.get(word, 0) + 1
print(rname)

# Top 30 words
#wlst = [(d[word], word) for word in d]
# sort list
#wlst.sort()
# count word totals descending
#wlst.reverse()
# print sentence elowe on new line
#print('\n The 30 most frequent words are\n')
# set i to 1
# print count of top 30 (from 1st word to 30th word) word (sums) from the text file 
#i = 1

# print repository dictionary 
# print(rname)

# with open('nihShort.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#                           #  quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     for count, word in wlst[:30]:
#        # spamwriter.writerow('%2s.,%4s,%s' % (i, count, word))
#         spamwriter.writerow([i, count, word])
#         i += 1




# %%

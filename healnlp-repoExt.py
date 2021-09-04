
import os

# empty list 
t = list()

# desktop path
desktopPath = '/Users/ousmanesow/Desktop/RSP_Analysis'

# open txt dataset with command that joins the file paths (ensures program can find objects easily)
with open(os.path.join(desktopPath, 'nihlong.txt'), 'r') as f:  
   # fhand = f.read()
    fhand = f.readlines()
    fhand = ' '.join(fhand)
    print(fhand)

# make everything lower characters 
fhand = fhand.lower()
# count characters in txt file
nchar = len(fhand)
print('Characters: ', nchar)
# count lines in txt file
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

# computing the total numer of words  
nwords = sum(d[word] for word in d )
print('number of words (without stop words): ', nwords)

# dictionary for repositories
rname = {'addgene': 0, 'ATCC':0, 'ICPSR': 0, 'pubchem': 0, 'openneuro': 0, 'openfmri': 0, 'dataverse': 0, 'dryad': 0, 'figshare': 0, 'mendeley data': 0, 'vivli': 0, 'zenodo':0, 'dash': 0, 'clinicalTrials': 0, 'xnat': 0, 'icpsr':0}

# loop for extracting repository names mentioned in txt file, and starting count
for word in words:
    #for word in list(d.keys()):
    if word in rname:
        rname[word] = rname.get(word, 0) + 1
print(rname)
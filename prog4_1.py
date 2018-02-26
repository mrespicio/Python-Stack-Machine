# By: Megan Respicio
# Date: December 2017
# Github: github.com/mrespicio

import sys
filename = sys.argv[-1]
f = open(filename, 'r')
lines = f.readlines()
for i in lines:
    word=i.split()
    print(', '.join(word))

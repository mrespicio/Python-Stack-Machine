import sys
print("Assignment #4-1, Megan Respicio, meganrespicio@hotmail.com")
filename = sys.argv[-1]
f = open(filename, 'r')
lines = f.readlines()
for i in lines:
    word=i.split()
    print(', '.join(word))

import sys
import StackMachine
filename = sys.argv[-1]
f = open(filename, 'r')
lines = f.readlines()
big = []
for i in lines:
    word=i.split()
    big=big+word
stack = StackMachine.StackMachine()

for j in range(len(big)):
    if big[j] == "push" and big[j+1].isdigit:
        stack.push(int(big[j+1]))
    if big[j] == "pop":
        stack.pop()
    if big[j] == "add":
        stack.add()
    if big[j] == "sub":
        stack.sub()
    if big[j] == "mul":
        stack.mul()
    if big[j] == "div":
        stack.div()
    if big[j] == "mod":
         stack.mod()

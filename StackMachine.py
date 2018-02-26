class StackMachine:
    def __init__(self):
        self.__data=[]
    def push(self, value):
        self.__data.append(value)
    def pop(self):
        return self.__data.pop()

    def add(self):
        if(len(self.__data)>1):
            self.push(self.pop() + self.pop())

    def sub(self):
        if(len(self.__data)>1):
            self.push(self.pop()-self.pop())

    def mul(self):
        if(len(self.__data)>1):
            self.push(self.pop()*self.pop())

    def div(self):
        if(len(self.__data)>1):
            self.push(self.pop()/self.pop())

    def mod(self):
        if(len(self.__data)>1):
            self.push(self.pop()%self.pop())

#    def display(self):
#        return self.__data
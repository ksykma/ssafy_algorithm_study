class Stack:
    def __init__(self):
        self.lst = []
    def empty(self):
        if self.lst == []:
            return True
        else:
            return False
    def top(self):
        if self.lst == []:
            return None
        else:
            return self.lst[-1]
    def pop(self):
        if self.lst == []:
            return None
        else:
            return self.lst.pop()
    def push(self, x):
        self.lst.append(x)
    def __repr__(self):
        return self

s1 = Stack()
print(s1.empty())
print(s1.top())
print(s1.pop())
s1.push('서영')
print(s1.empty())
print(s1.top())
print(s1.pop())
print(s1.empty())
class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if not self.values:
            print('Empty Stack')
        else:
            return self.values.pop()

    def peek(self):
        if not self.values:
            print('Empty Stack')
        else:
            return self.values[-1]

    def is_empty(self):
        if not self.values:
            return True
        return False

    def size(self):
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  
print(s.peek())  # распечатает 'dog'
s.push(True)  
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  
print(s.size())  # распечатает 2    

from ctypes.wintypes import tagPOINT
from queue import Empty


class Stack:
    '''Lifo'''
    class _Node:
        __slots__ = ['_element','_next']
        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element 
    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1
    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    def __str__(self):
        arr = ''
        start = self._head 
        for i in range(self._size):
            arr += str(start._element) + ','
            start = start._next
            return '<' + arr + ']'
S  = Stack()
def findPositionandDistance(P):
    s1 = Stack()
    s2 = Stack()
    s3 = Stack() 
    s4 = Stack()
    s5 = Stack()
    s6 = []
    i = 0
    x = 1 
    while i < len(P):
        if (P[i] == "("):
            s5.push(P[i])
            i += 1
            continue
        elif (P[i] == ")"):
            s5.pop()
            i +=1 
        elif P[i:i+2] == "+X":
            s1.push(x)
            s4.push(x)
        elif P[i:i+2] == "-X":
            s1.push(-x)
            s4.push(x)
        elif P[i:i+2] == "+Y":
            s2.push(x)
            s4.push(x)
        elif P[i:i+2] == "-Y":
            s2.push(-x)
            s4.push(x)
        elif P[i:i+2] == "+Z":
            s3.push(x)
            s4.push(x)
        elif P[i:i+2] == "-Z":
            s3.push(-x)
            s4.push(x)
        elif P[i].isnumeric():
            j = i + 1
            while P[j].isnumeric():
                j += 1
            t = eval(P[i:j])
            if len(s6) == 0:
                x = t
                s6.append(t)
            else:
                x = t*s6[2*len(s6)-len(s5) - 1]
                s6.append(t)
            i = j+1
            continue
        i += 2
    j,k,l,m = 0,0,0,0


    for i in range (len(s1)):
        j += s1._head._element
        s1.pop()
    for i in range (len(s2)):
        k += s2._head._element
        s2.pop()
    for i in range (len(s3)):
        l += s3._head._element
        s3.pop()
    for i in range (len(s4)):
        m += s4._head._element
        s4.pop()
    return [j,k,l,m]
print(findPositionandDistance("+X2(-Z-X+Y)8(+Y)9(-Z-Z)"))
print(findPositionandDistance("1(+X)5(+Y)41(+Z)1805(-X)3263441(-Y)10650056950805(-Z)"))
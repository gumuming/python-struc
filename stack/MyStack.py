

class ArrayStack:
    def __init__(self):
        self._data =[]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        return self._data.append(e)

    def top(self, e):
        if self.is_empty():
            raise Exception("Stack  is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack  is empty")
        return self._data.pop()


def reverse_file(filename):
    """
    读取文件 逆序输出 一行 一行
    """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() +"\n")
    output.close()
    
    
def is_matched(expr):
    """
    分隔符的匹配算法
    """
    
    lefty = '({['
    righty =')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            elif righty.index(c) != lefty.index(S.pop()):
                return False   
    return S.is_empty()


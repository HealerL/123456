# 一个头结点，左边指向队列开头，右边指向队尾
class Head(object):
    def ___init__(self):
        self.left = None
        self.right = None

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue(object):
    def __init__(self):
        self.head = Head()
    
    def enqueue(self, value):
        newnode = Node(value)
        p = self.head
        if p.right:
            #队列非空
            temp = p.right
            p.right = newnode
            temp.next = newnode
        else:
            #队列为空
            p.right = newnode
            p.left = newnode
    
    def dequeue(self):
        p = self.head
        if p.left and (p.left != p.right):
            # 不止一个元素
            temp = p.left
            p.left = temp.next
            return temp.value
        elif p.left and (p.left == p.right):
            #只有一个元素
            temp = p.left
            p.left = p.right = None
            return temp.value
        else:
            raise LookupError('queue is empty.')

    def isempty(self):
        if self.head.left:
            return False
        else:
            return True
    
    
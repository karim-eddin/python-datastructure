#encoding=utf-8

class Tree_Node:
    
    val = None
    lChild = None
    rChild = None
    parent = None
    height = None

    def __init__(self, val):
        self.val = val
        self.lChild = None
        self.rChild = None
        self.parent = None
        self.height = None
    
    def output(self):
        print(self.val, self.lChild, self.rChild, self.parent, self.height)


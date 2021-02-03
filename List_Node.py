#encoding=utf-8

class List_Node:
    val = None
    pNext = None

    def __init__(self, value):
        self.val = value

    def output(self):
        print(self.val)

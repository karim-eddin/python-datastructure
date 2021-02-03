#encoding=utf8

from Tree_Node import Tree_Node

class Tree:

    head = None
    tail = None

    def __init__(self):
        self.head = None
        self.tail = None
    
    def Pre_Order_Output(self):
        
        self.__PreOrder(self.head)
        print('*' *20)

    def __PreOrder(self, node):
        if None != node:
            print(node.val)

        if not None == node.lChild:
            self.__PreOrder(node.lChild)

        if not None == node.rChild:
            self.__PreOrder(node.rChild)
    
    def In_Order_Output(self):
        self.__InOrder(self.head)
        print('*' * 20)

    def __InOrder(self, node):

        if not None == node.lChild:
            self.__InOrder(node.lChild)
        if None != node:
            print(node.val)

        if not None == node.rChild:
            self.__InOrder(node.rChild)

    def Post_Order_Output(self):
        self.__PostOrder(self.head)
        print('*'*20)

    def __PostOrder(self, node):

        if not None == node.lChild:
            self.__PostOrder(node.lChild)

        if not None == node.rChild:
            self.__PostOrder(node.rChild)

        if None != node:
            print(node.val)
    

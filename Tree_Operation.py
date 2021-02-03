#coding=utf-8

from Tree_Node import Tree_Node

class SearchTree:

    root = None
    height = None

    def _insert(self, node, val):

        if val < node.val:
            if node.lChild != None:
                self._insert(node.lChild, val)
            else:
                node_tmp = Tree_Node(val)
                node.lChild = node_tmp
                node_tmp.parent = node
        elif val == node.val:
            print('double val')
        else:
            if node.rChild != None:
                self._insert(node.rChild, val)
            else:
                node_tmp = Tree_Node(val)
                node.rChild = node_tmp
                node_tmp.parent = node

    def insertNode(self, val):
        node = Tree_Node(val)

        if self.root == None:
            self.root = node
            self.root.height = 1
        else:
            self._insert(self.root, val)

    def searchVal(self, val):
        self.__search(self.root, val)

    def __search(self, node, val):
        if val == node.val:
            # print('found')
            return node
        
        if val < node.val:
            if node.lChild != None:
                return self.__search(node.lChild, val)
            else:
                print('not found')
                return None       

        if val > node.val:
            if node.rChild != None:
                return self.__search(node.rChild, val)
            else:
                print('not found')
                return None

    def output(self):

        if self.root == None:
            print('null tree')
        else:
            self.__output(self.root)
        
        print('-'*10)

    def __output(self,node):

        print(node.val)

        if node.lChild != None:
            self.__output(node.lChild)
        
        if node.rChild != None:
            self.__output(node.rChild)

    def deleteVal(self, val):

        node = self.__search(self.root, val)

        if node == None:
            print('node doesn\'t exist')

        self.adjustTree(node)
    
    def adjustTree(self,  node):

        #leaf node
        if node.lChild == None and node.rChild == None: 
            if node == node.parent.lChild:
                node.parent.lChild = None
            
            if node == node.parent.rChild:
                node.parent.rChild = None
        
        #one child node
        if node.lChild == None or node.rChild == None: 
            if node == node.parent.lChild: # node is the lft child of its parent
                if node.lChild != None:
                    node.parent.lChld = node.lChild
                    node.lChild.parent = node.parent
                elif node.rChild != None:
                    node.parent.lChild = node.rChild
                    node.lChild.parent = node.parent

            elif node == node.parent.rChild:
                if node.lChild != None:
                    node.parent.rChild = node.lChild
                    node.lChild.parent = node.parent
                elif node.rChild != None:
                    node.parent.rChild = node.rChild
                    node.rChild.parent = node.parent

        #two child node
        if node.lChild != None and node.rChild != None:

            rNode = None
            if node == node.parent.lChild:
                rNode = node.rChild
                while rNode != None:
                    rNode = rNode.lChild
                
                node_temp = Tree_Node(rNode.val)

                node_temp.lChild = node.lChild
                node_temp.rChild = node.rChild
                node_temp.parent = node.parent

            if node == node.parent.rChild:
                rNode = node.lChild
                while rNode != None:
                    rNode = rNode.rChild
                
                node_temp = Tree_Node(rNode.val)

                node_temp.lChild = node.lChild
                node_temp.rChild = node.rChild
                node_temp.parent = node.parent

        
            if rNode != None:
                self.adjustTree(rNode)

    def updateVal(self, oldVal, newVal):
        node = self.__search(self.root, oldVal)

        if node == None:
            print('node doesn\'t exist')
            return
        
        node.val = newVal


def main():

    tree = SearchTree()
    tree.insertNode('3')
    tree.insertNode('5')
    tree.insertNode('6')
    tree.insertNode('2')
    tree.searchVal('5')
    tree.output()
    tree.updateVal('6','8')
    tree.output()
    tree.deleteVal('5')
    tree.output()

if __name__ == '__main__':
    main()
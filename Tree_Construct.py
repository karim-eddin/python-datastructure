#encoding=utf-8


from Tree_Node import Tree_Node
from Tree_walkthrough import Tree

class Tree_Construct(Tree):
    
    Pre_Order_Seq = None
    In_Order_Seq = None
    Post_Order_Seq = None

    def __init__(self):
        self.Pre_Order_Seq = ''
        self.In_Order_Seq = ''
        self.Post_Order_Seq = ''

    
    def Construct_With_Pre_In(self):
        if len(self.Pre_Order_Seq)==0 or len(self.In_Order_Seq) == 0 \
        or len(self.Pre_Order_Seq) != len(self.In_Order_Seq):
            return 
        
        self.__Construct_With_Pre_In(self.Pre_Order_Seq, self.In_Order_Seq, None, None)


    def __Construct_With_Pre_In(self,  pre_order_seq, in_order_seq, root, child):

        rt = pre_order_seq[0] # Pre order first char is root
        rt_Node = Tree_Node(rt)
    
        if None == root:
            self.head = rt_Node
        else:
            if child == 'left':
                root.lChild = rt_Node
            elif child == 'right':
                root.rChild = rt_Node


        if len(pre_order_seq) == 1:
            return

        pos = in_order_seq.index(rt)

        left_in_order_seq = in_order_seq[0:pos]
        right_in_order_seq = in_order_seq[pos+1:]

        length_left = len(left_in_order_seq)
        length_right = len(right_in_order_seq)

        left_pre_order_seq = ''
        right_pre_order_seq = ''

        if length_left > 0:
            left_pre_order_seq = pre_order_seq[1:length_left+1]
    
        if length_right > 0:
            right_pre_order_seq = pre_order_seq[-length_right:]

        if len(left_pre_order_seq) > 0:
            self.__Construct_With_Pre_In(left_pre_order_seq, left_in_order_seq, rt_Node, 'left')

        if len(right_pre_order_seq) > 0:
            self.__Construct_With_Pre_In(right_pre_order_seq, right_in_order_seq, rt_Node, 'right')


    def Construct_With_In_Post(self):
        if len(self.Post_Order_Seq)==0 or len(self.In_Order_Seq) == 0 \
        or len(self.Post_Order_Seq) != len(self.In_Order_Seq):
            return 

        self.__Construct_With_In_Post(self.Post_Order_Seq, self.In_Order_Seq, None, None)

        
    def __Construct_With_In_Post(self, post_order_seq, in_order_seq, root, child):

        rt = post_order_seq[-1] # Post order last char is root
        rt_Node = Tree_Node(rt)
    
        if None == root:
            self.head = rt_Node
        else:
            if child == 'left':
                root.lChild = rt_Node
            elif child == 'right':
                root.rChild = rt_Node


        if len(post_order_seq) == 1:
            return

        pos = in_order_seq.index(rt)

        left_in_order_seq = in_order_seq[0:pos]
        right_in_order_seq = in_order_seq[pos+1:]

        length_left = len(left_in_order_seq)
        length_right = len(right_in_order_seq)

        left_post_order_seq = ''
        right_post_order_seq = ''

        if length_left > 0:
            left_post_order_seq = post_order_seq[:length_left]
    
        if length_right > 0:
            right_post_order_seq = post_order_seq[length_left:length_left +length_right]

        if len(left_post_order_seq) > 0:
            self.__Construct_With_In_Post(left_post_order_seq, left_in_order_seq, rt_Node, 'left')

        if len(right_post_order_seq) > 0:
            self.__Construct_With_In_Post(right_post_order_seq, right_in_order_seq, rt_Node, 'right')


def main():

    # tree = Tree_Construct()
    # tree.Pre_Order_Seq = 'GDAFEMHZ'
    # tree.In_Order_Seq = 'ADEFGHMZ'
    # tree.Construct_With_Pre_In()
    # tree.Pre_Order_Output()
    # tree.In_Order_Output()
    # tree.Post_Order_Output()

    tree = Tree_Construct()
    tree.Post_Order_Seq = 'AEFDHZMG'
    tree.In_Order_Seq = 'ADEFGHMZ'
    tree.Construct_With_In_Post()
    tree.Pre_Order_Output()
    tree.In_Order_Output()
    tree.Post_Order_Output()



if __name__ == '__main__':
    main()
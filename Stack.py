#encoding=utf-8

class Stack:

    stk_lst = []

    def top(self):
        if len(self.stk_lst) == 0:
            return None
        else:
            return self.stk_lst[-1]
    
    def length(self):
        
        return len(self.stk_lst)


    def pop(self):

        if len(self.stk_lst) == 0:
            return None
        else:
            self.stk_lst.pop()

    
    def push(self, value):
        
        self.stk_lst.append(value)

    
    def output(self):
        
        for val in self.stk_lst:
            print(str(val))



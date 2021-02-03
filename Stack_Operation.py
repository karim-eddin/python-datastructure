#encoding=utf-8

from Stack import Stack

def ParseParentheses(str_line):

    mapper = {}
    mapper['(']= ')'
    mapper['['] = ']'
    mapper['{'] = '}'

    valid_list = ['(',')','{','}','[',']']

    stk = Stack()

    str_lst = list(str_line)

    for str_word in str_lst:
      
        if str_word in valid_list:
            if str_word in mapper:
                stk.push(str_word)
            else: #need to match now
                if stk.length == 0:
                    return False

                if mapper[stk.top()] == str_word:
                    stk.pop()
                    continue
                else:
                    return False
    
    return True

def ParseLongestParentheses(str_line):

    mapper = {}
    mapper['(']= ')'
    mapper['['] = ']'
    mapper['{'] = '}'

    valid_list = ['(',')','{','}','[',']']

    stk = Stack()

    str_lst = list(str_line)

    max_length = 0
    cur_length = 0

    for str_word in str_lst:
        tmp_length = 0

        if str_word in valid_list:
            if str_word in mapper:
                stk.push(str_word)
            elif mapper[stk.top()] == str_word: #matched #need to match now
                    stk.pop()
                    cur_length = cur_length + 2
                    tmp_length = cur_length
                    
                    if stk.length() == 0:
                        cur_length = 0

            else: #not matched
                tmp_length = cur_length
                cur_length = 0

            if tmp_length > max_length:
                max_length = tmp_length
        
    return max_length

def ParseLongestParentheses_one(str_line):
    #only '(' and ')'
    stk = Stack()
    str_lst = list(str_line)
    max_length = 0

    for i in range(len(str_lst)):
        if '(' == str_lst[i]:
            stk.push(i)
        elif stk.length() != 0:
            max_length = max(max_length, i - stk.top() + 1)
            stk.pop()

    return max_length

def unit_test():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(4)
    stk.output()

    stk.pop()
    stk.output()

if __name__ == '__main__':

    str_line = '(()'

    print(ParseLongestParentheses_one(str_line))
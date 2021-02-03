#encoding=utf-8

#Manacher is to find the longest Palindrome substring
#normally, the time complexity is O(n2)
#In order to reduce the time complexity
#It tries to use the previous palindrome data
#to reduce the time complexsity to O(n)


def FindLongestPalindrome(str_line):

    p = [1]* len(str_line)
    mx = 1
    id = 0

    for i in range(1, len(str_line)):

        if mx > i:
            p[i] = min(p[2 * id - i], mx - i)        

        #update id and mx
        idx = p[i]
        while (i+idx) < len(str_line) and str_line[i - idx] == str_line[i + idx]:
            
            p[i] = p[i] + 1
            idx = idx + 1

            if p[i] + i > mx:
                mx = p[i] + i -1
                id = i

    
    print(max(p)*2-1)
    print(str_line[id - max(p)+1:id + max(p)])

def main():

    str_line = '12212321'
    FindLongestPalindrome(str_line)

if __name__ == '__main__':
    main()
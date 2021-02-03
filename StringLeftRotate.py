#encoding=utf-8

#time complexity O(kn), space complexity O(1)
def LeftRotateExhaustive(word, k):

    word_list = list(word)
    length = len(word_list)

    if length == 0:
        return

    #if k is large than word, get the remainder
    k = k % length

    for idx in range(k):
        chr = word_list[0]
        for cnt in range(length-1):
            word_list[cnt] = word_list[cnt + 1]
        
        word_list[-1] = chr
        
    return ''.join(word_list)

#time complexity O(n), space complexity O(k)
def LeftRotateCopy(word,k):

    word_list = list(word)
    length = len(word_list)

    if length == 0:
        return

    #if k is large than word, get the remainder
    k = k % length

    #create empty string, O(k)
    word_copy = ['']*length

    word_copy[:length-k] = word_list[k:length]
    word_copy[length-k:length] = word_list[0:k]

    return  ''.join(word_copy)


def ReverseString(word, start, end):
    
    word_list = list(word)

    #make sure start is less than end
    if start > end:
        start, end = end, start

    while(start < end):
        word_list[start], word_list[end-1] = word_list[end-1], word_list[start]
        start = start + 1
        end = end - 1

    # print(''.join(word_list))
    return ''.join(word_list)

#time complexity O(n), space complexity O(1)
def LeftRotateSwap(word, k):

    word_list = list(word)
    length = len(word_list)

    if length == 0:
        return

    #if k is large than word, get the remainder
    k = k % length

    word = ReverseString(word, 0, k)
    word = ReverseString(word, k, len(word))
    word = ReverseString(word, 0, len(word))

    return word


if __name__ == '__main__':

    word = 'This is only for test purpose!!'

    print(LeftRotateExhaustive(word,15))
    print(LeftRotateCopy(word, 15))
    print(LeftRotateSwap(word, 15))
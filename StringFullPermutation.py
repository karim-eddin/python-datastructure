#coding=utf-8

#time complexity O(kn), space complexity O(1)
def FullPermutationRecursion(word, start, end):
    
    if start == end:
        print(''.join(word))
        return

    for idx in range(start, end):

        #check for duplicate char, if the char to be swtiched is duplicate in the range start, idx
        #skip this char, for it's duplciate, and continue
        if word[idx] in word[start:idx]:
            continue

        word[start], word[idx] = word[idx] , word[start]
        FullPermutationRecursion(word, start + 1, end)
        word[idx], word[start] = word[start] , word[idx]

def ReverseString(word, start, end):
    
    #make sure start is less than end
    if start > end:
        start, end = end, start

    while(start < end):
        word[start], word[end-1] = word[end-1], word[start]
        start = start + 1
        end = end - 1


def CalculateNextPermutation(word):

    bfound = False

    for idx in range(len(word)-1,-1,-1):

        #skip the -1, 0 comparasion
        if idx == 0:
            break

        if word[idx-1] < word[idx]: #last ascent
            for cnt in range(len(word)-1, idx-1, -1):
                if word[cnt] < word[idx - 1]:
                    continue
                else:
                    word[idx-1], word[cnt] = word[cnt], word[idx-1]
                    ReverseString(word, idx, len(word))
                    bfound = True
                    return bfound
    
    return bfound


if __name__ == '__main__':

    word = '1234'
    word_list = list(word)

    # FullPermutationRecursion(word_list, 0, len(word_list))

    print(word_list)
    
    while(CalculateNextPermutation(word_list)):
        print(word_list)
#coding=utf-8

#time complexity O(kn), space complexity O(1)
def SubStringSearchBruteForce(word, substring):
    for idx in range(len(word)):
        
        bfound = True
        for cnt in range(len(substring)):
            if (word[idx+cnt]!=substring[cnt]):
                bfound = False
                continue
        
        if bfound == True:
            print(idx, word[idx:idx+len(substring)])
            break


#time complexity O(m+n), space complexity O(1)
def KMP_CalcNext(word):

    idx_k = -1
    idx_j = 0
    word_next = [0 for idx in range(len(word))] 
    word_next[0] = -1

    while idx_j < len(word) - 1:
        if idx_k == -1 or word[idx_j] == word[idx_k]:
            idx_j = idx_j + 1
            idx_k = idx_k + 1
            word_next[idx_j] = idx_k

        else:
            idx_k = word_next[idx_k]
            
    return word_next


def KMP_String(word, substring, subNext):

    idx = 0
    idx_k = 0
    bfound = False

    while idx < len(word):

        if idx_k == -1 or substring[idx_k] == word[idx]: #
            idx_k = idx_k + 1
            idx = idx + 1
        else:
            idx_k = subNext[idx_k]
        
        if idx_k == len(substring):
            bfound = True
            break

    if bfound:
        return idx - len(substring)
    else:
        return -1

if __name__ == '__main__':

    word = 'This is just one abaabc new test sample!!!'
    substring = 'abaabc'

    SubStringSearchBruteForce(word, substring)

    word_next = KMP_CalcNext(substring)

    print(KMP_String(word, substring, word_next))


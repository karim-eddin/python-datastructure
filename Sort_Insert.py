#encoding=utf-8

def SortInsert_For(data_list):

    for idx_i in range(1, len(data_list)):

        bInserted = False

        for idx_j in range(idx_i - 1,-1,-1):

            val = data_list[idx_j]
            if data_list[idx_j] < data_list[idx_i]:
                val = data_list.pop(idx_i)
                data_list.insert(idx_j+1, val)
                bInserted = True
                break
        
        if bInserted == False:
            val = data_list.pop(idx_i)
            data_list.insert(0, val)

#the benefit of the while is that when the while ended, the condition is not met
#but for 'for loop', it's uncertain, maybe it's finished, maybe it's condition is not met
#pay attentaion, the python could get the -1 index, so there should >0 constraint
def SortInsert_while(data_list):

    for idx_i in range(1, len(data_list)):

        idx_j = idx_i - 1

        while idx_j >= 0 and data_list[idx_j] > data_list[idx_i]:
            idx_j = idx_j - 1

        val = data_list.pop(idx_i)
        data_list.insert(idx_j+1, val)
        

def main():
    # data_list = [14,23,3,1,0,4,6,5,7,2,8]
    data_list = [4,6,5,7,2,3]

    # SortInsert_For(data_list)
    SortInsert_while(data_list)

    print(data_list)

if __name__ == '__main__':
    main()
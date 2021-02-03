#encoding=utf-8

def HeapAdjust(data_list, start_node, end):
    
    lChild = 2 * start_node + 1

    while (lChild < end ):

        if  lChild + 1 <= end and data_list[lChild] < data_list[lChild + 1]:
            lChild = lChild + 1
        
        #swap parent and bigger child
        if data_list[start_node] < data_list[lChild]:
            data_list[start_node] , data_list[lChild] = data_list[lChild] , data_list[start_node]
        else:
            break

        start_node = lChild
        lChild = start_node * 2 + 1


def HeapSort(data_list):
    
    end = len(data_list)-1
    while end > 0:

        data_list[0], data_list[end] = data_list[end], data_list[0]
        end = end - 1

        HeapAdjust(data_list, 0, end)
    
    print('sorted = ' + str(data_list))


def main():
    # data_lst = [14,23,3,1,0,4,6,5,7,2,8]
    data_lst = [4,6,5,7,2,3]

    #adjust to the big heap first
    for idx in range(int(len(data_lst) / 2 -1), -1, -1):
        HeapAdjust(data_lst, idx ,len(data_lst)-1)

    HeapSort(data_lst)


if __name__ == '__main__':
    main()
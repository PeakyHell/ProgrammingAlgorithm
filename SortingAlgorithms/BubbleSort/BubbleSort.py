def BubbleSort(list):
    for i in range(len(list), 0, -1):
        for j in range (1, i):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    return list
def SelectionSort(list):
    for i in range(0, len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]
    return list
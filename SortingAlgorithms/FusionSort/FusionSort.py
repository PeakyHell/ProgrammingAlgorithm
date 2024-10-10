def merge(list1, list2):
    list = []

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            list.append(list2[0])
            del list2[0]
        
        else:
            list.append(list1[0])
            del list1[0]

    while len(list1) > 0:
        list.append(list1[0])
        del list1[0]
    while len(list2) > 0:
        list.append(list2[0])
        del list2[0]

    return list


def fusionSort(list):
    if len(list) <= 1:
        return list
    
    half = len(list) // 2
    list1 = list[:half]
    list2 = list[half:]

    list1 = fusionSort(list1)
    list2 = fusionSort(list2)

    list = merge(list1, list2)

    return list
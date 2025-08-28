def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict.keys():
            print(j)
            return True
    return False


item_in_common((1,3,5), [2,4,5])
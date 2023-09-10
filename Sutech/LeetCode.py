l1 = [3, 4, 5]
l2 = [8, 5, 2, 5]


def sum_correcting(lst):
    j = 0
    while j != len(lst)-1:
        for i in range(len(lst)):
            if lst[i] >= 10:
                lst[i+1] += int((lst[i]-lst[i] % 10)/10)
                lst[i] = lst[i] % 10
        j += 1
    print(lst)


def sum_of_lists(lst1, lst2):
    sum_list = []
    lenght = min(len(lst1), len(lst2))

    for i in range(lenght):
        sum_list += [lst1[i]+lst2[i]]

    sum_correcting(sum_list)


sum_of_lists(l1, l2)

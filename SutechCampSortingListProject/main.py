def minimum(lst):
    mini = lst[0]
    for item in lst:
        if item<mini:
            mini=item
    return mini




def sort_number(lst):
    i =0
    while i<len(lst)-1:
        for num in lst[i+1:]:
            if num<lst[i]:
                temp = lst[i]
                lst[lst.index(num)]=lst[i]
                lst[i]=temp
                break
        i+=1
    return lst









nums=[4, 3, 6, 7, 1, 8, 3]
print(sort_number(nums))
print(minimum(nums))


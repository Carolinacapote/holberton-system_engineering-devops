#!/usr/bin/python3

def perfect_num(list):

    perfect_num = 0
    for i in list:
        counter = list.count(i)

        if i == counter:
            tmp = i
        if tmp > perfect_num:
            perfect_num = tmp

    if perfect_num != 0:
        return perfect_num
    else:
        return -1

list = [2, 2, 3, 3, 3, 4, 4, 4, 4]

perfect = perfect_num(list)
print(perfect)

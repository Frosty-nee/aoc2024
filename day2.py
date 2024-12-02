#! python3

import utils

def process_input(raw_input):
    return [[int(x) for x in line.split(" ")] for line in raw_input]

def count_perfectly_safe_paths(l):
    count = 0
    for line in l:
        if ((inc_or_dec(line) == 0) and (unsafe_levels(line) == 0)):
            count +=1
    return count

def unsafe_levels(l):
    count = 0
    for i in range(len(l)-1):
        if (abs(l[i] - l[i+1])> 3 or (l[i] == l[i+1])):
            count +=1
    return count

def inc_or_dec(l):
    inc, dec = 0, 0
    for i in range(len(l)-1):
        if (l[i+1] > l[i]): inc +=1
        if (l[i+1] < l[i]): dec +=1
    return (len(l)-1) - abs(inc-dec)


def count_safe_paths(l): #this is not ideal but I do not care
    count = 0
    for line in l:
        for c in range(len(line)):
            temp = line.copy()
            temp.pop(c)
            if ((inc_or_dec(temp)== 0 ) and( unsafe_levels(temp) == 0)):
                count +=1
                break
    return count

if __name__ == '__main__':
    data = process_input(utils.process_raw_input("inputs/day2.txt"))
    print(count_perfectly_safe_paths(data))
    print(count_safe_paths(data))
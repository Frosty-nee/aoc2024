#!python3

import utils

def process_input(lines):
    return [[int(line.split('   ')[0]) for line in lines],[int(line.split('   ')[1]) for line in lines]]

def calculate_distance(l1, l2):
    distance = 0
    for i in range(len(l1)):
        distance += abs(l1[i] - l2[i])
    return distance

def calculate_similarity(l1, l2):
    total = 0
    for line in l1:
        total += line*(l2.count(line))
    return total

if __name__ == '__main__':
    l1, l2 = process_input(utils.process_raw_input('inputs/day1.txt'))
    l1.sort(), l2.sort()
    print("Total Distance: {}".format(calculate_distance(l1, l2)))
    print("Similarity: {}".format(calculate_similarity(l1, l2)))
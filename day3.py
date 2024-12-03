#! python3

from utils import process_raw_input
import re

if __name__=='__main__':
    total = 0
    enable = True
    part2=False
    data = process_raw_input('inputs/day3.txt')
    for part in range(1,3):
        for line in data:
            for segment in re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)",line):
                    if segment == "do()": enable = True ; continue
                    elif segment == "don't()": enable = False; continue
                    else:
                        ft, st = list(map(int, segment[4:-1].split(',')))
                        if not part2: total += ft*st
                        if enable and part2: total += ft*st
        print("Part {}: {}".format(part, total))
        part2=True
        total = 0

#!python3

def process_raw_input(filepath):
    with open(filepath) as f:
        return [line.rstrip() for line in f.readlines()]
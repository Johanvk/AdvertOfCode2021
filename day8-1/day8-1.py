"""part 1 of Day 8 Advent of Code 2021"""

from typing import List, Tuple, Dict, Set
import time
start_time = time.time()

def fetch_segments() -> List[str]:
    """Returns the 10 segments list and display in a list from input file"""  
    segment_list = []
    with open("day8-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = line.replace('|','').strip()
            temp_list = x.split()
            segment_list.append(temp_list)
    return segment_list

def parse_segments(segment_list: List[str]) -> int:
    """ find the numbers 1 (lenght 2), 4 (lenght 4), 7(lenght 3), 8(lenght 7) """
    total_unique = 0
    for x in range(200):
        for y in range(10, 14):
            z = len(segment_list[x][y])
            if z == 2 or z == 3 or z == 4 or z == 7:
                total_unique += 1
    return total_unique

def main():
    segment_list = fetch_segments()
    total_unique = parse_segments(segment_list)
    print(total_unique)
    
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
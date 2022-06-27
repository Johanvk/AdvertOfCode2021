"""part 1 of Day 5 Advent of Code 2021"""

from typing import List, Tuple, Set
import time
start_time = time.time()
  
def fetch_coordinates() -> Tuple[List[int], List[int], List[int]]:
    """Returns the horizontal, vertical and diagonal points from input file"""  
    x = 0
    horizontal = []
    vertical =[]
    diagonal = []
    with open("day5-1.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = line.replace(' -> ',',')
            vector = [int(s) for s in x.split(",")]
            if vector[0] == vector[2]:
                horizontal.append(vector)
            elif vector[1] == vector[3]:
                vertical.append(vector)
            else:
                diagonal.append(vector)
        return horizontal, vertical, diagonal

def grit(horizontal: List[int]) -> int:
    """" returns the grit size """
    temp_grit_size = 0
    number_entries = len(horizontal)
    for x in range(number_entries):
        temp_entry = str(horizontal[x][0])
        if len(temp_entry) > temp_grit_size:
            temp_grit_size = len(temp_entry)
    grit_size = 10 ** temp_grit_size
    return grit_size
    
def parse_hor(horizontal, grit_size: Tuple[List[int], int]) -> Tuple[set, set]:
    index_set = set()
    more_two = set()
    number_entries = len(horizontal)
    for x in range(number_entries):
        if horizontal[x][1] > horizontal[x][3]:
            for y in range(horizontal[x][3], horizontal[x][1] + 1):
                index = y * grit_size + horizontal[x][0]
                if index in index_set:
                    more_two.add(index)
                else:
                    index_set.add(index)
        else:
            for y in range(horizontal[x][1], horizontal[x][3] + 1):
                index = y * grit_size + horizontal[x][0]
                if index in index_set:
                    more_two.add(index)
                else:
                    index_set.add(index)				
    return index_set, more_two
  
def parse_ver(vertical, grit_size, index_set, more_two: Tuple[List[int], int, set, set]) -> Tuple[set, set]:
    number_entries = len(vertical)
    for x in range(number_entries):
        if vertical[x][0] > vertical[x][2]:
            for y in range(vertical[x][2], vertical[x][0] + 1):
                index = vertical[x][1] * grit_size + y
                if index in index_set:
                    more_two.add(index)
                else:
                    index_set.add(index)
        else:
            for y in range(vertical[x][0], vertical[x][2] + 1):
                index = vertical[x][1] * grit_size + y
                if index in index_set:
                    more_two.add(index)
                else:
                    index_set.add(index)				
    return index_set, more_two    
 
    
def main():
    horizontal, vertical, diagonal = fetch_coordinates()
    grit_size = grit(horizontal)
    index_set, more_two = parse_hor(horizontal, grit_size)
    index_set, more_two = parse_ver(vertical, grit_size, index_set, more_two)
    print("the number of crossings =", len(more_two))  
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
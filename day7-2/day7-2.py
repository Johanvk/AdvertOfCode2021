"""part 2 of Day 7 Advent of Code 2021"""

from typing import List, Tuple, Dict, Set
from sys import maxsize
import time
start_time = time.time()

def fetch_crab() -> Tuple[List[int], set]:
    """Returns the crab list and set from input file"""  
    with open("day7-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            crab_list = [int(s) for s in line.split(',')]
            break
        crab_set = set(crab_list)
        return crab_list, crab_set

def find_cal_range(crab_set: set) -> set:
    """ exclude first 200 and last 200 from the set to limit calculations """
    temp_list = list(crab_set)
    for x in range(200):
        y = temp_list[x]
        crab_set.remove(y)
    for x in range(1,200):
        y = temp_list[-x]
        crab_set.remove(y)
    return crab_set
        
def calculate_fuel(crab_list, crab_set: Tuple[List[int], set]) -> Dict[int,int]:
    """ Calculate teh fuel for each position """
    crab_dict = {}
    lowest_crab_fuel = maxsize
    crab_fuel = maxsize
    count = 0
    """ count is used to limit unneaded calculations, crab_dict is for debug """
    for x in crab_set:
        if crab_fuel < lowest_crab_fuel and count < 25:
            lowest_crab_fuel = crab_fuel
        crab_fuel = 0
        for y in crab_list:
                if crab_fuel >= lowest_crab_fuel or count > 25:
                    count += 1
                    break
                elif x >= y:
                    crab_fuel += sum(range((x-y) + 1))
                    crab_dict[x] = crab_fuel 
                else: 
                    crab_fuel += sum(range((y-x) + 1))
                    crab_dict[x] = crab_fuel
    return lowest_crab_fuel
        
    
def main():
    crab_list, crab_set = fetch_crab()
    crab_set = find_cal_range(crab_set)
    lowest_crab_fuel = calculate_fuel(crab_list, crab_set)
    print(lowest_crab_fuel)
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
    
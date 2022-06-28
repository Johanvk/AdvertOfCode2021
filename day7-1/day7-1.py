"""part 1 of Day 7 Advent of Code 2021"""

from typing import List, Tuple, Dict, Set
from sys import maxsize
import time
start_time = time.time()

def fetch_crab() -> Tuple[List[int], set]:
    """Returns the crab list and set from input file"""  
    crab_dict = {}
    with open("day7-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            crab_list = [int(s) for s in line.split(',')]
            break
        crab_set = set(crab_list)
        return crab_list, crab_set

def calculate_fuel(crab_list, crab_set: Tuple[List[int], set]) -> Dict[int,int]:
    """ Calculate teh fuel for each position"""
    crab_dict = {}
    for x in crab_set:
        crab_fuel = 0
        for y in crab_list:
            if x >= y:
                crab_fuel += (x-y)
                crab_dict[x] = crab_fuel 
            else: 
                crab_fuel += (y-x)
                crab_dict[x] = crab_fuel 
    return crab_dict

def find_lowest(crab_dict, crab_set: Tuple[Dict[int,int], set]) -> set:
    """ return the lowest ammount of fuel used"""
    least_fuel = maxsize
    for x in crab_set:
        if least_fuel > crab_dict[x]:
            least_fuel = crab_dict[x]
    return least_fuel
        
    
def main():
    crab_list, crab_set = fetch_crab()
    crab_dict = calculate_fuel(crab_list, crab_set)
    least_fuel = find_lowest(crab_dict, crab_set)
    print(least_fuel)
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
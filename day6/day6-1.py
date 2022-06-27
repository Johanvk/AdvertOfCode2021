"""part 1 of Day 6 Advent of Code 2021"""

from typing import List, Tuple, Dict
import time
start_time = time.time()

def fetch_fish() -> Dict[int,int]:
    """Returns the fish and counter value from input file"""  
    fish_dict = {}
    with open("day6-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            fish_list = [int(s) for s in line.split(',')]
            break
        for x in range(10):
            fish_dict[x] = 0
            count = 0
            for fish in fish_list:
                if x == fish:
                    count += 1
                    fish_dict[x] = count
        return fish_dict

def calculate_fish(fish_dict, days: Tuple[Dict[int,int], int]):
    temp_dict = {}
    for x in range(days):
        temp_dict = fish_dict
        for y in range(9):
            fish_dict[y] = temp_dict[y + 1]
        fish_dict[9] = temp_dict[0] 
        fish_dict[6] = temp_dict[8] + temp_dict[6]    
    return fish_dict



def main():
    fish_dict = fetch_fish()
    days = 256
    fish_dict = calculate_fish(fish_dict, days) 
    total_fish = fish_dict[0] + fish_dict[1] + fish_dict[2] + fish_dict[3] + fish_dict[4] + fish_dict[5] + fish_dict[6] + fish_dict[7] + fish_dict[8]
    print(total_fish)
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
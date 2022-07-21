"""part 1 of Day 11 Advent of Code 2021"""

from typing import List, Dict, Tuple
import time
start_time = time.time()


def read_data_file() -> Tuple[Dict[int,int], int]:
    """ Returns the a dictionary from input file """  
    octopus_dict = {}
    key = 0
    number_lines = 0
    with open("day11-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            number_lines += 1
            for item in line.strip():
                octopus_dict[key] = int(item)
                key += 1
    return octopus_dict, number_lines
    

def increase_one(octopus_dict: Dict[int,int]) -> Tuple[Dict[int,int], List[int]]: 
    """ Increase each value by 1 and check for flashes and return octopus_dict and a dict with flashes (value 10)"""
    flash_list = []
    for key in range(len(octopus_dict)):
        octopus_dict[key] = octopus_dict[key]+1
        if octopus_dict[key] == 10:
            flash_list.append(key)
            octopus_dict[key] = 0  
    return octopus_dict, flash_list


def claculate_grid(octopus_dict, temp_keylist: Tuple[Dict[int,int], List[int]]) -> Tuple[Dict[int,int], List[int]]:
    """ Raise the surrounding keys with 1 after a octopus reaches 10"""
    additional_flash = []
    for tempkey in temp_keylist:
        if octopus_dict[tempkey] != 0:
            octopus_dict[tempkey] = octopus_dict[tempkey]+1
            if octopus_dict[tempkey] == 10:
                additional_flash.append(tempkey)
                octopus_dict[tempkey] = 0
    return octopus_dict, additional_flash                


def secondary_flash(octopus_dict, flash_list: Tuple[Dict[int,int], List[int]]) -> Tuple[Dict[int,int], List[int]]:
    """ Calculate secondary flashes"""
    additional_flash_list = []
    for key in flash_list:
        # check the corners
        if key == 0:
            temp_keylist = [key+1, key+10, key+11]
        elif key == 9:
            temp_keylist = [key-1, key+9, key+10]
        elif key == 90:    
            temp_keylist = [key-10, key-9, key+1]
        elif key == 99:    
            temp_keylist = [key-11, key-10, key-1]
        # check first and last row
        elif key < 9:
            temp_keylist = [key-1, key+1, key+9, key+10, key+11]
        elif key > 90:
            temp_keylist = [key-11, key-10, key-9, key-1, key+1]
        # check first and last colom
        elif key % 10 == 0:    
            temp_keylist = [key-10, key-9, key+1, key+10, key+11]
        elif key % 10 == 9:    
            temp_keylist = [key-11, key-10, key-1, key+9, key+10]
        # others
        else:
            temp_keylist = [key-11, key-10, key-9, key-1, key+1, key+9, key+10, key+11]
        octopus_dict, additional_flash = claculate_grid(octopus_dict, temp_keylist)
        additional_flash_list.extend(additional_flash)
    return octopus_dict, additional_flash_list


def calculate_energy(octopus_dict, number_lines: Tuple[Dict[int,int], int]) -> int:
    """ calculate the energy and flashes of the octupus after 100 steps"""
    steps = 100
    flashes = 0
    for x in range(steps):
        octopus_dict, flash_list = increase_one(octopus_dict)
        flashes += len(flash_list)
        while len(flash_list) != 0:
            octopus_dict, additional_flash_list = secondary_flash(octopus_dict, flash_list)
            flashes += len(additional_flash_list)
            flash_list = additional_flash_list.copy() 
    return flashes
    
    
def main():
    """ get input from file and calculate the flashes"""
    octopus_dict, number_lines = read_data_file()
    flashes = calculate_energy(octopus_dict, number_lines)
    print("Total_flash", flashes)

   
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
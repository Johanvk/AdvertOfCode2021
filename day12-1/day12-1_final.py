"""part 1 of Day 12 Advent of Code 2021"""

from typing import List, Tuple
import time
start_time = time.time()


def read_data_file() -> List[List[str]]:
    """ Returns the a list of cave connections from input file """  
    cave_conn = []
    temp_list = []
    with open("day12-1_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            temp_list = [s.strip() for s in line.split('-')]
            cave_conn.append(temp_list)
    return cave_conn
    

def find_start_points(cave_conn: List[List[str]]) -> Tuple[List[List[str]], List[List[str]]]:
    """ Return a list of start points and a updated cave connection list """
    start_list = []
    org_start_list =[]
    for connection in cave_conn:
        temp_list = []
        if 'start' in connection[0]:
            start_list.append(connection)
            org_start_list.append(connection)
        elif 'start' in connection[1]:
            temp_list.append(connection[1])
            temp_list.append(connection[0])
            start_list.append(temp_list)
            org_start_list.append(connection)
    for start in org_start_list:
        cave_conn.remove(start)
    return cave_conn, start_list


def find_path(cave_conn, start, start_to_end: Tuple[List[List[str]], List[str], List[List[str]]]) -> Tuple[List[List[str]], List[List[str]]]:
    """ Process the start point list and return updated temp path list and start to end list"""
    temp_path_list = []
    for cave in cave_conn:
        temp_start = []
        temp_start = start.copy()
        if temp_start[-1] == cave[0]:
            temp_start.append(cave[1])
            if cave[1] == 'end': 
                start_to_end.append(temp_start)
            elif cave[1].islower() and cave[1] in start:
                continue
            else:
                temp_path_list.append(temp_start)
        elif temp_start[-1] == cave[1]:
            temp_start.append(cave[0])
            if cave[0] == 'end': 
                start_to_end.append(temp_start)
            elif cave[0].islower() and cave[0] in start:
                continue
            else:
                temp_path_list.append(temp_start)
    return temp_path_list, start_to_end
    

def find_cave_path(cave_conn, start_list: Tuple[List[List[str]], List[List[str]]]) -> List[List[str]]:
    """ find the cave paths from the start points"""
    start_to_end = []
    while len(start_list) != 0:
        start = start_list.pop(0)
        temp_path_list, start_to_end = find_path(cave_conn, start, start_to_end)
        for path in temp_path_list: 
            start_list.append(path)
    return start_to_end
    
    
def main():
    """ get input from file and calculate the flashes"""
    cave_conn = read_data_file()
    cave_conn, start_list = find_start_points(cave_conn)
    start_to_end = find_cave_path(cave_conn, start_list)
    print(f"Number of paths, {len(start_to_end)}")
    
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
 
 
 
    
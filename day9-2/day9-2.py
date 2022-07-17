"""part 2 of Day 9 Advent of Code 2021"""

from typing import List, Tuple, Set
import time
start_time = time.time()

num_rows = 0

def fetch_input() -> List[str]:
    """ Returns the a list from input file.""" 
    input_list = []
    with open("day9-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = list(line.strip())
            y = [int(v) for v in x]
            input_list.append(y)
        return input_list


def find_low_points(input_list: List[str]) -> List[List[str]]:
    """ Collect a list of low points (row, colom, value) """
    low_list = []
    row_num = len(input_list)
    col_num = len(input_list[0])
    for row in range(row_num):
        for y in range(col_num):
            # check the corners
            if row == 0 and y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row +1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
            elif row == 0 and y == col_num -1:
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row +1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
            elif row == row_num -1 and y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row -1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
            elif row == row_num -1 and y == col_num -1: 
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row -1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
            # process first and last colom
            elif y == col_num -1:
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row -1][y] and input_list[row][y] < input_list[row +1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list) 
            elif y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row -1][y] and input_list[row][y] < input_list[row +1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
            # check the rows
            elif input_list[row][y -1] > input_list[row][y] and input_list[row][y] < input_list[row][y + 1]:
                if row == 0 and input_list[row][y] < input_list[row + 1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
                elif row == row_num -1 and input_list[row][y] < input_list[row - 1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)
                elif input_list[row][y] < input_list[row - 1][y] and input_list[row][y] < input_list[row + 1][y]:
                    temp_list = [row, y, input_list[row][y]]
                    low_list.append(temp_list)                
    return low_list

def up_check(input_list, temp_point, up_list, basin_set: Tuple[List[List[int]], List[int], List[List[int]], set]) -> List[int]:
    """" From point check up direction"""
    count = 9 - temp_point[2]
    while count > 0:
        if temp_point[0] == 0:
            break
        elif input_list[temp_point[0]-1][temp_point[1]] < 9:
            y = [temp_point[0]-1, temp_point[1], input_list[temp_point[0]-1][temp_point[1]], temp_point[3], 'up']
            if y[0] * num_rows + y[1] not in basin_set:
                up_list.append(y)
                temp_point = y
                basin_set.add(temp_point[0] * num_rows + temp_point[1])
                count -= 1
            else:
                break
        else:
            break 
    return up_list, basin_set 


def down_check(input_list, temp_point, down_list, basin_set: Tuple[List[List[int]], List[int], List[List[int]], set]) -> List[int]:
    """" From point check down direction"""
    count = 9 - temp_point[2]
    while count > 0:
        if temp_point[0] == num_rows -1: 
            break
        elif input_list[temp_point[0] +1][temp_point[1]] < 9:
            y = [temp_point[0] +1, temp_point[1], input_list[temp_point[0] +1][temp_point[1]], temp_point[3],'down']
            if y[0] * num_rows + y[1] not in basin_set:
                down_list.append(y)
                temp_point = y
                basin_set.add(temp_point[0] * num_rows + temp_point[1])
                count -= 1
            else:
                break
        else:
            break 
    return down_list, basin_set       
  
    
def left_check(input_list, temp_point, left_list, basin_set: Tuple[List[List[int]], List[int], List[List[int]], set]) -> List[int]:
    """" From point check left direction"""
    count = 9 - temp_point[2]
    while count > 0:
        if temp_point[1] == 0: 
            break
        elif input_list[temp_point[0]][temp_point[1] -1] < 9:
            y = [temp_point[0], temp_point[1]-1, input_list[temp_point[0]][temp_point[1]-1], temp_point[3],'left']
            if y[0] * num_rows + y[1] not in basin_set:
                left_list.append(y)
                temp_point = y
                basin_set.add(temp_point[0] * num_rows + temp_point[1])
                count -= 1
            else:
                break
        else:
            break 
    return left_list, basin_set             


def right_check(input_list, temp_point, right_list, basin_set: Tuple[List[List[int]], List[int], List[List[int]], set]) -> List[int]:
    """" From point check right direction"""
    count = 9 - temp_point[2]
    while count > 0:
        if temp_point[1] == num_rows -1: 
            break
        elif input_list[temp_point[0]][temp_point[1] +1] < 9:
            y = [temp_point[0], temp_point[1]+1, input_list[temp_point[0]][temp_point[1] +1], temp_point[3],'right']
            if y[0] * num_rows + y[1] not in basin_set:
                right_list.append(y)
                temp_point = y
                basin_set.add(temp_point[0] * num_rows + temp_point[1])
                count -= 1
            else:
                break
        else:
            break 
    return right_list, basin_set          


def check_point(input_list, temp_point: Tuple[List[List[int]], List[int]]) -> Tuple[List[int], set]:
    """" Find the basin from zero point"""
    global num_rows
    num_rows = len(input_list[0])
    point_list = []
    point_list.append(temp_point)
    basin_set = {temp_point[0] * num_rows + temp_point[1]}
    if temp_point[0] > 0:
        total_result, basin_set = up_check(input_list, temp_point, point_list, basin_set)
    if temp_point[0] < num_rows -1:
        total_result, basin_set = down_check(input_list, temp_point, point_list, basin_set)
    if temp_point[1] > 0:
        total_result, basin_set = left_check(input_list, temp_point, point_list, basin_set)
    if temp_point[1] < num_rows -1:
        total_result, basin_set = right_check(input_list, temp_point, point_list, basin_set)
    #print("lenght", len(total_result))
    for value in total_result:
        total_result, basin_set = left_check(input_list, value, point_list, basin_set)
        total_result, basin_set = right_check(input_list, value, point_list, basin_set)
        total_result, basin_set = up_check(input_list, value, point_list, basin_set)
        total_result, basin_set = down_check(input_list, value, point_list, basin_set) 
    #print("lenght", len(total_result))
    return total_result, basin_set




def main():
    """ get input from file, find low points and calculate basins"""
    a = 0
    b = 0
    c = 0
    input_list = fetch_input()
    low_point = find_low_points(input_list)
    for point in range(len(low_point)):
        temp_point = low_point[point]
        temp_point.extend([point, 'zero'])
        total_result, basin_set = check_point(input_list, temp_point)
        # find the top three basins
        if a <= b and a <= c or a == 0:
            if len(basin_set) > a:
                a = len(basin_set)
        elif b <= a and b <= c or b == 0:        
            if len(basin_set) > b:
                b = len(basin_set)
        elif c <= a and c <= b or c == 0:           
            if len(basin_set) > c:
                c = len(basin_set)  
    print("Total of three basins", a * b * c)
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
          
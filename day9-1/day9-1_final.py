""" Part 1 of Day 9 Advent of Code 2021 """

from typing import List
import time
start_time = time.time()

def fetch_input() -> List[str]:
    """ Returns a list from input file """  
    input_list = []
    with open("day9-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = list(line.strip())
            y = [int(v) for v in x]
            input_list.append(y)            
        return input_list

def find_low_points(input_list: List[str]) -> int:
    count_low = 0
    row_num = len(input_list)
    col_num = len(input_list[0])
    for row in range(row_num):
        for y in range(col_num):
            # check the corners
            if row == 0 and y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row +1][y]:
                    count_low += input_list[row][y] +1
            elif row == 0 and y == col_num -1: 
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row +1][y]:
                    count_low += input_list[row][y] +1
            elif row == row_num -1 and y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row -1][y]:
                    count_low += input_list[row][y] +1
            elif row == row_num -1 and y == col_num -1: 
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row -1][y]:
                    count_low += input_list[row][y] +1   
            # process first and last colom
            elif y == col_num -1:
                if input_list[row][y] < input_list[row][y - 1] and input_list[row][y] < input_list[row -1][y] and input_list[row][y] < input_list[row +1][y]:
                    count_low += input_list[row][y] +1  
            elif y == 0:
                if input_list[row][y] < input_list[row][y + 1] and input_list[row][y] < input_list[row -1][y] and input_list[row][y] < input_list[row +1][y]:
                    count_low += input_list[row][y] +1
            # check the rows
            elif int(input_list[row][y -1]) > int(input_list[row][y]) and input_list[row][y] < input_list[row][y + 1]:
                if row == 0 and input_list[row][y] < input_list[row + 1][y]:
                    count_low += input_list[row][y] +1
                elif row == row_num -1 and input_list[row][y] < input_list[row - 1][y]:
                    count_low += input_list[row][y] +1
                elif input_list[row][y] < input_list[row - 1][y] and input_list[row][y] < input_list[row + 1][y]:
                    count_low += input_list[row][y] +1                        
    return count_low
        
def main():
    input_list = fetch_input()
    count_low = find_low_points(input_list)
    print("The sum of all low points", count_low)

if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    

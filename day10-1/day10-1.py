"""part 1 of Day 10 Advent of Code 2021"""

from typing import List, Tuple
from operator import countOf
import queue
import time
start_time = time.time()


def read_data_file() -> List[List[str]]:
    """ Returns the a list of lists from input file """  
    character_list = []
    with open("day10-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = list(line.strip())
            character_list.append(x)
    return character_list
  

def get_illegal_character(line: List[str]) -> str:
    """ Find the invalid character and return the value or None"""
    qcharacter = queue.LifoQueue()
    for value in line:
        if value in ['{', '(', '[', '<']:
            qcharacter.put(value)
        else:
            item = qcharacter.get()
            if item == '{' and value != '}' or item == '[' and value != ']' or item == '(' and value != ')' or item == '<' and value != '>':
                #print('invalid character', item, value)
                return value
                break 
    return None
 
        
def find_illegal_characters(character_list: List[List[str]]) -> List[str]:
    """ returns a list of illegal characters"""
    illegal_characters = []
    for line in character_list:
        illegal_characters.append(get_illegal_character(line))
    return illegal_characters   
     
   
def cal_total_score(illegal_characters: List[str]) -> int: 
    """ Calculate the total score of the illegal characters"""
    """
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
    """
    score = 0
    point_dict = {')': 3, ']': 57, '}': 1197, '>': 25137} 
    for character in ['}', ']', '>', ')']:
        count = countOf(illegal_characters, character)
        print(f'{character}, {count}')
        score += count * point_dict[character]
    return score


def main():
    """ get input from file"""
    character_list = read_data_file()
    illegal_characters = find_illegal_characters(character_list)
    score = cal_total_score(illegal_characters)
    print(" total score illegal characters", score)
   
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
"""part 2 of Day 10 Advent of Code 2021"""

from typing import List
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
  

def get_missing_character(line: List[str]) -> str:
    """ Find the missing characters and return the list or x on illegal lines"""
    qcharacter = queue.LifoQueue()
    missing_characters = []
    invalid_character = False
    for value in line:
        if value in ['{', '(', '[', '<']:
            qcharacter.put(value)
        else:
            item = qcharacter.get()
            if item == '{' and value != '}' or item == '[' and value != ']' or item == '(' and value != ')' or item == '<' and value != '>':
                #print('missing character', item, value)
                invalid_character = True
                break 
    if invalid_character == True:
        return 
    for character_in_queue in range(qcharacter.qsize()):
        item = qcharacter.get()
        missing_characters.append(item)
    return missing_characters
 
        
def find_missing_characters(character_list: List[List[str]]) -> List[str]:
    """ returns a list of missing characters"""
    missing_characters = []
    for line in character_list:
        result = get_missing_character(line)
        if result != None:
            missing_characters.append(result)
    return missing_characters   
     
   
def cal_middle_score(missing_characters: List[str]) -> int: 
    """ Calculate the total score of the illegal characters"""
    """
    (: 1 point.
    [: 2 points.
    {: 3 points.
    <: 4 points.
    """
    score_list = []
    point_dict = {'(': 1, '[': 2, '{': 3, '<': 4} 
    for x in range(len(missing_characters)):
        score = 0
        for character in missing_characters[x]:
            score = score * 5 + point_dict[character]
        score_list.append(score)
    score_list.sort()
    middle_score = score_list[int(len(score_list)/2)]
    return middle_score


def main():
    """ get input from file"""
    character_list = read_data_file()
    missing_characters = find_missing_characters(character_list)
    middle_score = cal_middle_score(missing_characters)
    print(f"Middle score of missing characters: {middle_score}")
   
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
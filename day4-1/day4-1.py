"""part 1 of Day 4 Advent of Code 2021"""

from typing import List, Tuple

def fetch_bingo() -> Tuple[List[int], List[int]]:
    """Returns bingo cards and bingo numbers from input file"""
    bingo_numbers = []
    templine = []
    board = []
    all_boards = []
    with open("day4-1.txt", "r", encoding="utf-8") as values:
        for line in values:
            if len(bingo_numbers) == 0:
                bingo_numbers = [int(s) for s in line.split(",")]
            elif line != '\n':
                templine = line.split()
                for x in templine:
                    board.append(int(x))
                if len(board) == 25:
                    copy_board = board.copy()
                    all_boards.append(copy_board)
            else:
                board.clear()
    return all_boards, bingo_numbers

def generate_sets(number_of_bords: int) -> List[int]:
    """" generate a list of sets used as index """
    x = 0
    all_sets = []
    temp_set = set()
    while x < number_of_bords:
        for y in range(25):
            temp_set.add(y)
        x += 1
        copy_set = temp_set.copy() 
        all_sets.append(copy_set)
    return all_sets

def parse_boards(number_of_bords, all_numbers, all_boards, all_sets: Tuple[int, List[int], List[int], List[int]]) -> int:
    """ parse the bingo cards and if bingo equals True return final score """
    for bingo_number in all_numbers:
        x = -1
        while x < number_of_bords -1:
            x += 1
            temp_set = all_sets[x].copy()
            for y in temp_set:
                check_num = all_boards[x][y]
                if bingo_number == check_num:
                    all_sets[x].remove(y)
                    bingo = check_bingo(all_sets[x], all_boards[x])
                    if bingo == True:
                        tot_left =0
                        for index in all_sets[x]:
                            tot_left += all_boards[x][index]
                        final_score = tot_left * all_boards[x][y]
                        print("Board", x, "number", all_boards[x][y])
                        return final_score
                        
                        
                        
def check_bingo(check_set, left_numbers: Tuple[List[int], List[int]]):
    for i in range(5):
        for j in range(5):
            if i * 5 + j in check_set:
                break
        else:
            return True
        for j in range(5):
            if i + 5 * j in check_set:
                break
        else:
            return True
    else:
        return False 
        

def main():
    all_boards, bingo_numbers = fetch_bingo()
    number_of_bords = len(all_boards)
    all_sets = generate_sets(number_of_bords)
    final_score = parse_boards(number_of_bords, bingo_numbers, all_boards, all_sets) 
    print("The final score", final_score)
    
    
if __name__ == "__main__":
    main()




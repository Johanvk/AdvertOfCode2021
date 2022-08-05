"""part 1 of Day 13 Advent of Code 2021"""

from typing import List, Tuple
import time
start_time = time.time()


class Get_Data:
    def __init__(self):
        self.dot_list = []
        self.fold_list = []
        

    def read_data_file(self):
        with open("day13-1_input.txt", "r", encoding="utf-8") as input:
            for line in input:
                if ',' in line:
                    temp_list = [s.strip() for s in line.split(',')]
                    temp_list = [int(s) for s in temp_list]
                    self.dot_list.append(temp_list)
                elif 'along' in line:
                    temp_list = [s.strip() for s in line.split('along')]
                    temp_list = [s for s in temp_list[1].split('=')]
                    temp_list[1] = int(temp_list[1])
                    self.fold_list.append(temp_list)
        return self.dot_list, self.fold_list

        
class Process_Code:
    def __init__(self):
        self.folded_paper = []
        self.foldxy_list = []
        

    def fold_x(self, fold_line: int):
        temp_fold_list = self.folded_paper.copy()
        for point in range(len(temp_fold_list)):
            if temp_fold_list[point][0] > fold_line:
                x = (fold_line * 2) - temp_fold_list[point][0]
                if [x, temp_fold_list[point][1]] in self.folded_paper:
                    self.folded_paper.remove(temp_fold_list[point])
                else:
                    self.folded_paper.append([x, temp_fold_list[point][1]])
                    self.folded_paper.remove(temp_fold_list[point])
        
		
    def fold_y(self, fold_line: int):
        temp_fold_list = self.folded_paper.copy()
        for point in range(len(temp_fold_list)):
            if temp_fold_list[point][1] > fold_line:
                y = (fold_line * 2) - temp_fold_list[point][1]
                if [temp_fold_list[point][0], y] in self.folded_paper:
                    self.folded_paper.remove(temp_fold_list[point])
                else:
                    self.folded_paper.append([temp_fold_list[point][0], y])
                    self.folded_paper.remove(temp_fold_list[point])
                    

    def fold_paper(self):
        print(self.foldxy_list)
        pass
    
    
    def first_fold(self):
        if self.foldxy_list[0][0] == 'x':
            self.fold_x(self.foldxy_list[0][1])
        elif self.foldxy_list[0][0] == 'y':
            self.fold_y(self.foldxy_list[0][1])
        return self.folded_paper
        
    
def main():
    """ get input from file and calculate the flashes"""
    get_input = Get_Data()
    dots, folds = get_input.read_data_file()
    print(f"proccessed data file, dots:\n {dots}\n")
    print(f"the fold lines, folds:\n {folds}\n")
    activation_code = Process_Code()
    activation_code.foldxy_list = folds.copy()
    activation_code.folded_paper = dots.copy()
    first_fold_points = activation_code.first_fold()
    print(f"number of points after first fold: {len(first_fold_points)}")
  
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))
 
 
 
    
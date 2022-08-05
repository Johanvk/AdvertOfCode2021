"""part 2 of Day 13 Advent of Code 2021"""


import time
start_time = time.time()


class GetData:
    """ Retrieve data """
    def __init__(self):
        self.dot_list = []
        self.fold_list = []


    def read_data_file(self):
        """ Retrieve data from file"""
        with open("day13-1_input.txt", "r", encoding="utf-8") as input_data:
            for line in input_data:
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


class ProcessCode:
    """ process point on paper"""
    def __init__(self):
        self.folded_paper = []
        self.foldxy_list = []
        self.digit_list = []


    def fold_x(self, fold_line: int):
        """ fold the paper on line """
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
        """ fold the paper on the y axel """
        temp_fold_list = self.folded_paper.copy()
        for point in range(len(temp_fold_list)):
            if temp_fold_list[point][1] > fold_line:
                y = (fold_line * 2) - temp_fold_list[point][1]
                if [temp_fold_list[point][0], y] in self.folded_paper:
                    self.folded_paper.remove(temp_fold_list[point])
                else:
                    self.folded_paper.append([temp_fold_list[point][0], y])
                    self.folded_paper.remove(temp_fold_list[point])
                 

    def first_fold(self):
        """ Dtermine the number of points after the first fold"""
        if self.foldxy_list[0][0] == 'x':
            self.fold_x(self.foldxy_list[0][1])
        elif self.foldxy_list[0][0] == 'y':
            self.fold_y(self.foldxy_list[0][1])
        return self.folded_paper


    def find_digit(self):
        """ find the eight digits """
        for digit in range(8):
            temp_list = []
            for point in self.folded_paper:
                temp_point = []
                if point[0] in range(digit * 5, (digit+1) *5):
                    temp_point = point.copy()
                    temp_point[0] = point[0]-digit*5
                    temp_list.append(temp_point)
            temp_list.sort()
            self.digit_list.append(temp_list)
            #print(digit, temp_list)


    def decode_digit(self) -> str:
        """ Decode the digits to letters and return the 8 letter code """
        code = ''
        L = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 5], [2, 5], [3, 5]]
        C = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 5], [2, 0], [2, 5], [3, 1], [3, 4]]
        F = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 2], [2, 0], [2, 2], [3, 0]]
        P = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 3], [2, 0], [2, 3], [3, 1], [3, 2]]
        K = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 2], [2, 1], [2, 3], [2, 4], [3, 0], [3, 5]]
        for digit in self.digit_list:
            if digit == L:
                code += 'L'
            elif digit == C:
                code += 'C'
            elif digit == F:
                code += 'F'
            elif digit == P:
                code += 'P'
            elif digit == K:
                code += 'K'
            else:
                print("manual decode needed, digit not present in code book")
        return code


    def fold_paper(self):
        """ process the paper by applying all the folds """
        for fold in self.foldxy_list:
            if fold[0] == 'x':
                self.fold_x(fold[1])
            elif fold[0] == 'y':
                self.fold_y(fold[1])


    def process_paper(self) -> str:
        """ Process the paper by folding, find the digits and return the code """
        self.fold_paper()
        self.find_digit()
        code = self.decode_digit()
        return code


def main():
    """ get input from file and calculate the flashes"""
    get_input = GetData()
    dots, folds = get_input.read_data_file()
    activation_code = ProcessCode()
    activation_code.foldxy_list = folds.copy()
    activation_code.folded_paper = dots.copy()
    first_fold_points = activation_code.first_fold()
    print(f"number of points after first fold: {len(first_fold_points)}\n")
    activation_code.folded_paper = dots.copy()
    code = activation_code.process_paper()
    print(f"The code to activate imaging camera system = {code}\n")


if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

    
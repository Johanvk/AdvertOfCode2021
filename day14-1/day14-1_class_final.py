""" part 2 of Day 14 Advent of Code 2021"""

from collections import Counter
import time
start_time = time.time()


class GetData:
    """ Retrieve data from an input file"""
    def __init__(self):
        self.polymer = ''
        self.insertion_rules = {}


    def read_data_file(self):
        """ Import the data from file """
        with open("day14-1_input.txt", "r", encoding="utf-8") as input_data:
            for line in input_data:
                if '\n' == line:
                    continue
                elif '->' not in line:
                    temp_list = [s.strip() for s in line.split('->')]
                    self.polymer = temp_list[0]
                elif '->' in line:
                    temp_list = [s.strip() for s in line.split('->')]
                    self.insertion_rules[temp_list[0]] = temp_list[1]
        return self.polymer, self.insertion_rules


class Polymerization:
    """ Processor polymer"""
    def __init__(self):
        self.polymer_str = ''
        self.insertion_rules = {}


    def polymer_increase(self):
        """ Polymer increase """
        temp_polymer_str = ''
        for x in range(len(self.polymer_str)-1):
            if len(temp_polymer_str) == 0:
                temp_polymer_str += self.polymer_str[0]
            element = self.insertion_rules[self.polymer_str[x:x+2]]
            temp_polymer_str += element
            temp_polymer_str += self.polymer_str[x+1]
        self.polymer_str = temp_polymer_str


    def calculate_elements(self) -> int:
        """calculate the number of each element and return the iff between most/least """
        counts_element = Counter(list(self.polymer_str))
        all_values = counts_element.values()
        return max(all_values) - min(all_values)


    def polymer_processor(self, number_steps: int) -> int:
        """ calculate the expension of polymer and return the diff between max - min """
        print(f"Number of steps processed = {number_steps}\n")
        for step in range(number_steps):
            self.polymer_increase()
        result_max_min = self.calculate_elements()
        return result_max_min


def main():
    """ get input from file and calculate the flashes"""
    get_input = GetData()
    polymer_start, insertion_rules = get_input.read_data_file()
    # start of polymer processing
    number_steps = 10
    process_polymer = Polymerization()
    process_polymer.polymer_str = polymer_start
    process_polymer.insertion_rules = insertion_rules
    result_max_min = process_polymer.polymer_processor(number_steps)
    print(f"The most common element minus the least common element = {result_max_min}\n")

if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

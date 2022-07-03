"""part 1 of Day 8 Advent of Code 2021"""

from typing import List, Tuple, Dict, Set
import time
start_time = time.time()

def fetch_segments() -> Tuple[List[str], List[str]]:
    """Returns the segments and display list from input file"""  
    segment_list = []
    display_list =[]
    temp_list_seg = []
    with open("day8-1_input.txt", "r", encoding="utf-8") as values:
        for line in values:
            x = line.replace('|','').strip()
            temp_list = x.split()
            temp_list_seg.append(temp_list)
    for x in range(len(temp_list_seg)):
        temp_list1 = temp_list_seg[x][10:14]
        temp_list2 = temp_list_seg[x][0:10]
        display_list.append(temp_list1)
        segment_list.append(temp_list2)
    return segment_list, display_list

def decode_segments(segment_list: List[str]) -> List[Dict]:
    """ Decode the segments and return a dict with the results """
    temp_list_five = []
    temp_list_six = []
    decode_list = []
    for x in range(len(segment_list)):
        decode_dict = {}
        temp_list = segment_list[x]
        temp_list_five.clear()
        temp_list_six.clear()
        for y in range(10):
            if len(temp_list[y]) == 2:
                decode_dict["".join(sorted(temp_list[y]))] = '1'
            elif len(temp_list[y]) == 3:
                decode_dict["".join(sorted(temp_list[y]))] = '7'
                seven_set = set(temp_list[y])
            elif len(temp_list[y]) == 4:
                decode_dict["".join(sorted(temp_list[y]))] = '4'
                four_set = set(temp_list[y])
            elif len(temp_list[y]) == 7:
                decode_dict["".join(sorted(temp_list[y]))] = '8'  
            elif len(temp_list[y]) == 5:
                temp_list_five.append("".join(sorted(temp_list[y])))
            else:
                temp_list_six.append("".join(sorted(temp_list[y])))
        for y in range(3):
            if seven_set.issubset(set(temp_list_six[y])) == False:
                decode_dict[temp_list_six[y]] = '6'
                six_set = temp_list_six[y]
            elif four_set.issubset(set(temp_list_six[y])) == True:
                decode_dict[temp_list_six[y]] = '9'
            else:
                decode_dict[temp_list_six[y]] = '0'
        for y in range(3):
            if seven_set.issubset(set(temp_list_five[y])) == True:
                decode_dict[temp_list_five[y]] = '3'
            elif set(temp_list_five[y]).issubset(six_set) == True:
                decode_dict[temp_list_five[y]] = '5'
            else:
                decode_dict[temp_list_five[y]] = '2'
        decode_list.append(decode_dict)    
    return decode_list   
     
        
def decode_display(decode_list, display_list: Tuple[List[Dict], List[str]]) -> int:
    """ Decode the displays and return the sum of the values """
    total_display = 0
    for x in range(len(display_list)):
        temp_display = []
        for y in range(4):
            key = "".join(sorted(display_list[x][y]))
            temp_display.append(decode_list[x][key])
        total_display += int("".join(temp_display))
    return total_display

    
def main():
    segment_list, display_list = fetch_segments()
    decode_list = decode_segments(segment_list)
    total_display = decode_display(decode_list, display_list)
    print("The total of all displays =", total_display)
  
    
if __name__ == "__main__":
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))



    
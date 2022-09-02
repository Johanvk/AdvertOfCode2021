""" part 1 of Day 15 Advent of Code 2021"""

from typing import List, Tuple
import time



class GetData:
    """ Retrieve data from an input file"""
    def __init__(self):
        pass


    def read_data_file(self) -> Tuple[int, int, List[List[int]]]:
        node_cost_dict = {}
        """ Import the data from file """
        rows = 0
        with open("day15-1_input.txt", "r", encoding="utf-8") as input_data:
            for line in input_data:
                position = 0 
                x = list(line.strip())
                y = [int(v) for v in x]
                coloms = len(y)
                for node in y:
                    node_cost_dict[rows*coloms+position] = node
                    position += 1
                rows += 1
        return rows, coloms, node_cost_dict


class RiskProcessor:
    """ process the risk map"""
    def __init__(self):
        self.node_cost ={}
        self.visited_node_set = set()
        self.lowest_cost_node = 0
        self.temp_node_dict = {}
        self.calculated_risk = {}


    def find_neighbors(self, rows,coloms: int):
        """ Create an list of neighbors for the lowest_cost_node """
        neighbor_list = []
        #check corners
        if self.lowest_cost_node == 0:
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node+coloms)
        elif self.lowest_cost_node == coloms-1:
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node+coloms)
        elif self.lowest_cost_node == (rows-1)*coloms:
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node-coloms)
        elif self.lowest_cost_node == (rows*coloms)-1:
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node-coloms)
        #check edges
        elif self.lowest_cost_node < coloms-1:
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node+coloms)
        elif self.lowest_cost_node%coloms == 0:
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node-coloms)
            neighbor_list.append(self.lowest_cost_node+coloms)
        elif (self.lowest_cost_node+1)%coloms == 0:
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node-coloms)
            neighbor_list.append(self.lowest_cost_node+coloms)
        elif self.lowest_cost_node > (coloms)*(rows-1):
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node-coloms)
        #provide neighbors around
        else:
            neighbor_list.append(self.lowest_cost_node-1)
            neighbor_list.append(self.lowest_cost_node+1)
            neighbor_list.append(self.lowest_cost_node-coloms)
            neighbor_list.append(self.lowest_cost_node+coloms)
        return neighbor_list


    def risk_calculator(self,rows,coloms: int):
        """run dijkstra and return the node with the lowest cost from the top left to the bottom corner right"""
        self.temp_node_dict[0] = [0,0]
        destination_node = rows*coloms-1
        while destination_node != self.lowest_cost_node:
            neighbor_list = self.find_neighbors(rows,coloms)
            #print(neighbor_list)
            for node in neighbor_list:
                cost_temp = self.temp_node_dict[self.lowest_cost_node][0] + self.node_cost[node]
                if node in self.visited_node_set:
                    continue
                elif node not in self.temp_node_dict.keys():
                    self.temp_node_dict[node] = [cost_temp, node]
                elif cost_temp < self.temp_node_dict[node][0]:
                    self.temp_node_dict[node][0] = cost_temp
                    print("update", node, self.temp_node_dict[node], cost_temp)
            self.visited_node_set.add(self.lowest_cost_node)
            self.calculated_risk[self.lowest_cost_node] = self.temp_node_dict[self.lowest_cost_node]
            del self.temp_node_dict[self.lowest_cost_node]
            temp_lowest_list = list(self.temp_node_dict.values())
            temp_lowest_list.sort()
            self.lowest_cost_node = temp_lowest_list[0][1]
            #print("lowest", self.lowest_cost_node, temp_lowest_list[0][0])
        #print(self.calculated_risk)
        return self.lowest_cost_node, temp_lowest_list[0][0]


def main():
    """ get input from file and calculate the flashes"""
    get_input = GetData()
    rows, coloms, node_cost = get_input.read_data_file()
    #process path
    find_shortest_path = RiskProcessor()
    find_shortest_path.node_cost = node_cost
    node, lowest_cost = find_shortest_path.risk_calculator(rows, coloms)
    print(f"lowest cost for node {node} = {lowest_cost}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

# Class to read in and manage address and distances
import csv


class LocationCollection:
    # Initialize list of addresses and distances
    # Read CSV file
    def __init__(self):
        self.addresses = []
        self.distances = []
        self.read_file()

    # Read CSV file, first 27 lines are address names, the rest are distance values to each address O(n)
    def read_file(self):

        with open("WGUPS Distance Table final.csv") as distance_file:
            distance_data = list(csv.reader(distance_file, delimiter=","))

            for val in range(27):
                self.addresses.append(distance_data[val][1].strip())

            for val2 in range(27, len(distance_data)):
                self.distances.append(distance_data[val2])

    # Function to return the index of address in list of addresses O(1)
    def index_for_address(self, address):
        return self.addresses.index(address)

    # Function to return all addresses O(1)
    def get_addresses(self):
        return self.addresses

    # Function to get distance value between two addresses using address index
    # If value returns nothing, check reverse 0(1)
    def get_distance(self, row, col):
        distance = self.distances[row][col]
        if distance == "":
            distance = self.distances[col][row]

        return float(distance)

    # Function to get distance between two addresses by converting to address index and calling get_distance() O(1)
    def get_distance_between_addresses(self, address1, address2):
        return self.get_distance(self.index_for_address(address1), self.index_for_address(address2))

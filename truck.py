# Class to store Truck information
import datetime


class Truck:
    # Initialize truck with time of departure from hub and list of packages O(1)
    def __init__(self, leave_time):
        self.leave_time = datetime.datetime.strptime(leave_time, "%H:%M:%S")
        self.items = []
        self.max_items = 16
        self.speed = .005                                   # MPH converted to Miles per second for datetime convenience
        self.location = "4001 South 700 East"

    # Add package to Truck O(1)
    def add_item(self, item):
        self.items.append(item)

    # Remove package from truck O(1)
    def remove_item(self, item):
        self.items.remove(item)

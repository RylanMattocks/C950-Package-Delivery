# Class to store Driver information
from locations import LocationCollection
from datetime import timedelta
from package_manager import wgu_packages


class Driver:
    # Initialize Driver with truck and store route of packages O(1)
    def __init__(self):
        self.truck = None
        self.locations = LocationCollection()
        self.package_route = []

    # Function to deliver packages to each location O(n^2)
    def deliver_packages(self, return_to_hub=False, check_time=False, time=None, package_id=0):
        current_time = self.truck.leave_time        # Retrieve departure time from Truck
        self.get_route()                            # Get delivery route from function
        arrival_time = None                         # Initialize Truck arrival time at location
        total_distance = 0                          # Initialize total distance traveled by truck
        all_delivered = False                       # Initialize all delivered to False

        # Set items in truck to en route
        if check_time and self.truck.leave_time < time:
            for item in self.package_route:
                item.status = "En Route"

        # Loop for truck to deliver packages
        for item in self.package_route:
            # Get and set Distance and time to location
            distance_to_location = self.locations.get_distance_between_addresses(self.truck.location, item.address)
            time_to_location = distance_to_location/self.truck.speed
            arrival_time = current_time + timedelta(seconds=time_to_location)

            # If truck is in route and all items need printed (check_time) print all items and leave loop
            if (check_time and arrival_time > time and int(package_id) == 0) or (all_delivered and int(package_id) == 0):
                for item in self.package_route:
                    item.print()
                break
            # If truck is in route and single item needs printed (check_time) print item and leave loop
            if (check_time and arrival_time > time and int(package_id) == item.id) or (all_delivered and int(package_id) == item.id):
                item.print()
                break

            item.status = "Delivered"                      # Set package status to Delivered
            item.delivery_time = arrival_time.time()       # Set package delivery time

            current_time = arrival_time             # Set current time to arrival time at location
            self.truck.location = item.address      # Set trucks current location to package address
            total_distance += distance_to_location  # Update total distance traveled

        # Trucks are not required to return to hub at end of day
        # Check to see if Driver needs to return to hub to pick up different truck
        # If driver needs to return, calculate distance and time to return truck to hub
        if return_to_hub:
            distance_to_location = self.locations.get_distance_between_addresses(self.truck.location, "4001 South 700 East")
            time_to_location = distance_to_location / self.truck.speed
            arrival_time = current_time + timedelta(seconds=time_to_location)
            total_distance += distance_to_location

        all_delivered = True                # Initialize all delivered to True
        # Check if each package in route is delivered if not set all delivered to False
        for item in self.package_route:
            if item.status != "Delivered":
                all_delivered = False

        # If all packages have been delivered and items need printed
        if all_delivered and check_time:
            item_ids = []                                   # Make list to hold all item ids on truck

            # Fill item ids list with all ids in truck
            for item in self.package_route:
                item_ids.append(item.id)

            # If package ID is in item ids list then set index and print package
            if int(package_id) in item_ids:
                index = item_ids.index(int(package_id))
                self.package_route[index].print()

            # Otherwise print all items
            else:
                for item in self.package_route:
                    item.print()

        return arrival_time, total_distance

    ###############################################################################################
    # ***** Pseudo Code for Nearest Neighbor Algorithm *****
    # While items_in_route[] is not equal to total_items_in_truck[]:
    #   sorted list = sort items_in_truck[], get distance between current location and package addresses and sort based
    #                                        on shortest distance
    #   for each package in sorted list:
    #       if package is not in current route:
    #           add package to route and update current location
    ##############################################################################################

    # Nearest Neighbor Algorithm to find best route for truck to deliver packages O(n^2)
    def get_route(self):

        location = self.truck.location

        while len(self.package_route) != len(self.truck.items):
            sorted_items = sorted(self.truck.items, key=lambda item: self.locations.get_distance_between_addresses(location, item.address))
            for item in sorted_items:
                if item not in self.package_route:
                    self.package_route.append(item)
                    location = item.address
                    break

# Rylan Mattocks, ID: 000939513


# A.  Identify a named self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”)
#   that you used to create your program to deliver the packages.
#
# I used nearest neighbor algorithm


# B.  Write an overview of your program, in which you do the following:
# 1.  Explain the algorithm’s logic using pseudocode.
#
# See driver.py

# 2.  Describe the programming environment you used to create the Python application.
#
# I used PyCharm

# 3.  Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O notation.
#
# Notation is in comments throughout code

# 4.  Explain the capability of your solution to scale and adapt to a growing number of packages.
#
# The scalability of the project is rather small. As of now, if no packages came in with a deadline, then
# one truck would not be filled at all. Leaving the maximum packages the code could currently handle at 32.
# With small adjustments to the amount of trucks and packages that are hard coded to a specific value it could
# scale much better.

# 5.  Discuss why the software is efficient and easy to maintain.
#
# The program begins the first truck at the start of the day with all packages that need to be delivered by a deadline.
# After that the second truck waits for any package that needs the address updated and begins to deliver packages after
# that time. The third truck then leaves soon after the first truck returns to the hub. The program is not overly
# complex and therefore easy to update and maintain.

# 6.  Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).
#
# The hash table created is great for the package information because the key (package ID) directly corresponds with the
# bucket. A major weakness is because each key has its own bucket, the memory required to hold packages is increased
# with each package added. For the amount of data required for the project this hash table is very efficient and doesn't
# require large amounts of memory to be used in storing the information.


# D.  Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm identified
#   in part A to store the package data.
#
# See hash_table.py
#
# 1.  Explain how your data structure accounts for the relationship between the data points you are storing.
#
# The hash table stores each package as a list of all the item components. The list is then stored in a bucket based on
# the package ID number. To access the package you can search the package ID number and it will return a list with each
# component of the package. Then you can use the index or loop through the entire package to view the requested
# information.


# E.  Develop a hash table, without using any additional libraries or classes, that has an insertion function
#   that takes the following components as input and inserts the components into the hash table:
# •   package ID number
# •   delivery address
# •   delivery deadline
# •   delivery city
# •   delivery zip code
# •   package weight
# •   delivery status (e.g., delivered, en route)
#
# See hash_table.py


# F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:
# •   package ID number
# •   delivery address
# •   delivery deadline
# •   delivery city
# •   delivery zip code
# •   package weight
# •   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time
#
# See hash_table.py


# G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time,
#   and the total mileage traveled by all trucks. (The delivery status should report the package as
#   at the hub, en route, or delivered. Delivery status must include the time.)
# 1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
#
# See attached file "All package Status at 09:00:00.pdf"

# 2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
#
# See attached file "All package Status at 10:00:00.pdf"

# 3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.
#
# See attached file "All package Status at 13:00:00.pdf"


# H.  Provide a screenshot or screenshots showing successful completion of the code, free from runtime errors
#   or warnings, that includes the total mileage traveled by all trucks.
#
# See attached file "Completion of Code with Total Mileage.pdf"


# I.  Justify the core algorithm you identified in part A and used in the solution by doing the following:
# 1.  Describe at least two strengths of the algorithm used in the solution.
#
# Two strengths of the nearest neighbor algorithm used that it is not complex and easy to implement. Also, while it is
# not the most efficient, it is very efficient in setting a route for delivery. The algorithm itself finds the shortest
# from the current location to a package on the truck. Therefore the algorithm itself is only as efficient as the
# loading process of the packages on the truck.

# 2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
#
# The algorithm delivers each of the packages by their deadline, and has a total mileage of less that 140 miles.

# 3.  Identify two other named algorithms, different from the algorithm implemented in the solution,
#   that would meet the requirements in the scenario.
#
# Dijkstra's Algorithm and Heuristic Algorithm
# a.  Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.
#
# Dijkstra's Algorithm would choose the shortest route possible given the packages in each truck. Rather than choosing
# the closest package to the current location it would search every possible route and find the route that would be the
# least total distance to travel. A heuristic algorithm would be less optimal. It would sort the packages by closest to
# the hub and deliver in that order. It would be a quicker execution since it does not need to check the distance
# from every location to the next closest, but the route would be much less efficient.


# J.  Describe what you would do differently, other than the two algorithms identified in I3, if you did this project again.
#
# I would want to develop a better approach to assigning the packages to each truck. Currently if no package has a
# delivery deadline, then one truck will not be used to deliver packages making the max packages 32. Also, I would want
# to make the program more easily expandable to allow more drivers and trucks possibly by making the total number of
# each a value that can be modified by a variable.


# K.  Justify the data structure you identified in part D by doing the following:
# 1.  Verify that the data structure used in the solution meets all requirements in the scenario.
#
# The hash table stores all the package information in a list. Each list is stored based on the package ID.
# a.  Explain how the time needed to complete the look-up function is affected by changes in the number of packages to be delivered.
#
# The time needed to look up each package would remain the same if the number of packages increased. The hash table is
# designed to store each package in its own bucket so if more packages are added, more memory must also be used to store
# the package info. Looking up package ID 1 would get index one from the hash table which would be the same time as
# looking up package ID 100 by getting the 100th index of the hash table.
# b.  Explain how the data structure space usage is affected by changes in the number of packages to be delivered.
#
# The amount of space used by the hash table is directly related to the amount of packages. Each package gets its own
# bucket so 10 packages would need 10 buckets and 100 packages would need 100 buckets.
# c.  Describe how changes to the number of trucks or the number of cities would affect the look-up time and
#   the space usage of the data structure.
#
# The number of trucks and cities would increase the space usage and look up time would increase all at the same rate.

# 2.  Identify two other data structures that could meet the same requirements in the scenario.
#
# Set and Array
# a.  Describe how each data structure identified in part K2 is different from the data structure used in the solution.
#
# A set would allow the storage of all package information and not allow duplicates. This would work well since each
# package has a unique package ID therefore allowing no insertion of duplicate packages. An array would store the data
# as an unordered list and without knowing the index the lookup of each item would be worst case O(n) where as the hash
# table is O(1)

import package_manager
from driver import Driver
import datetime

# User Interface
print("C950 Routing Program")

# Variables to store user input O(1)
user_exit = "quit"
user_input = None

# Loop to get user input until user inputs "quit" O(n^2)
while user_input != user_exit:
    # Statement to request user input
    user_input = input("\nSelect an option or type 'quit' to quit:\n"
                       "1. View single package info at specific time\n"
                       "2. View all package info at specific time\n"
                       "3. View EOD Delivery info\n")

    # If user inputs 1 O(n^2)
    if user_input == "1":
        package_exists = False                  # Check if package exists
        trucks = package_manager.initialize()   # Initialize Trucks
        drivers = [Driver(), Driver()]          # Initialize Drivers
        drivers[0].truck = trucks[0]            # Set Driver 1 to Truck 1
        drivers[1].truck = trucks[1]            # Set Driver 2 to Truck 2

        # Get package Id from User
        user_package_id = input("Enter a package ID: ")

        # Check if item is in a truck and if so package exists
        for item in trucks[0].items:
            if item.id == int(user_package_id):
                package_exists = True
        for item in trucks[1].items:
            if item.id == int(user_package_id):
                package_exists = True
        for item in trucks[2].items:
            if item.id == int(user_package_id):
                package_exists = True

        # If package doesn't exist prompt user and return to beginning
        if package_exists is False:
            print("Invalid Package ID")
            continue

        # Get time from user
        user_time = input("Enter a time in 24H Format (HH:MM:SS): ")
        # Check to see if input is in correct time format if not prompt user and return to beginning
        try:
            datetime.datetime.strptime(user_time, '%H:%M:%S')
        except ValueError:
            print("Incorrect format")
            continue

        user_date_time = datetime.datetime.strptime(user_time, '%H:%M:%S')  # Format user time to datetime object

        # Loop through first truck route and if package ID is in truck print package
        for item in trucks[0].items:
            if item.id == int(user_package_id):
                driver1_return_time, driver1_total_distance = drivers[0].deliver_packages(True, True, user_date_time,
                                                                                          user_package_id)
        # Loop through second truck route and if package ID is in truck print package
        for item in trucks[1].items:
            if item.id == int(user_package_id):
                driver2_return_time, driver2_total_distance = drivers[1].deliver_packages(False, True, user_date_time,
                                                                                          user_package_id)

        drivers[0].package_route = []       # Reset driver 1's route
        drivers[0].truck = trucks[2]        # Set driver 1 to Truck 3

        # Loop through third truck route and if package ID is in truck print package
        for item in trucks[2].items:
            if item.id == int(user_package_id):
                driver3_return_time, driver3_total_distance = drivers[0].deliver_packages(False, True, user_date_time,
                                                                                          user_package_id)
    # If user input is 2 O(n^2)
    elif user_input == "2":

        trucks = package_manager.initialize()   # Initialize Trucks
        drivers = [Driver(), Driver()]          # Initialize Drivers
        drivers[0].truck = trucks[0]            # Set driver 1 to truck 1
        drivers[1].truck = trucks[1]            # Set driver 2 to truck 2

        # Get time from user
        user_time = input("Enter a time in 24H format (HH:MM:SS): ")
        # Check to see if input is in correct time format if not prompt user and return to beginning
        try:
            datetime.datetime.strptime(user_time, '%H:%M:%S')
        except ValueError:
            print("Incorrect format")
            continue
        user_date_time = datetime.datetime.strptime(user_time, '%H:%M:%S')  # Format user time to datetime object

        # Print all packages at given time for truck 1
        driver1_return_time, driver1_total_distance = drivers[0].deliver_packages(True, True, user_date_time)
        # Print all packages at given time for truck 2
        driver2_return_time, driver2_total_distance = drivers[1].deliver_packages(False, True, user_date_time)
        drivers[0].package_route = []       # Reset driver 1's route
        drivers[0].truck = trucks[2]        # Set driver 1 to truck 3
        # Print all packages at given time for truck 3
        driver3_return_time, driver3_total_distance = drivers[0].deliver_packages(False, True, user_date_time)

    # If user input is 3 O(n^2)
    elif user_input == "3":
        trucks = package_manager.initialize()   # Initialize Trucks
        drivers = [Driver(), Driver()]          # Initialize Drivers
        drivers[0].truck = trucks[0]            # Set driver 1 to truck 1
        drivers[1].truck = trucks[1]            # Set driver 2 to truck 2

        # Print packages at end of route for truck 1
        driver1_return_time, driver1_total_distance = drivers[0].deliver_packages(True)
        # Print packages at end of route for truck 2
        driver2_return_time, driver2_total_distance = drivers[1].deliver_packages()
        drivers[0].package_route = []       # Reset driver 1's route
        drivers[0].truck = trucks[2]        # Set driver 1 to truck 3
        # Print packages at end of route for truck 3
        driver3_return_time, driver3_total_distance = drivers[0].deliver_packages()

        # Add total distance of each truck
        total_distance = driver1_total_distance + driver2_total_distance + driver3_total_distance

        # Print total distance of all trucks and what time each truck finishes route
        print("Total Distance Traveled: ", total_distance, "\nTruck 1 Finishes at: ", driver1_return_time.time(),
              "\nTruck 2 Finishes at: ", driver2_return_time.time(), "\nTruck 3 Finishes at: ", driver3_return_time.time())

    # If user inputs quit then exit program O(1)
    elif user_input == "quit":
        print("Program Exited")
        exit()

    # If user inputs any unaccepted value prompt user and return to beginning
    else:
        print("Invalid input")

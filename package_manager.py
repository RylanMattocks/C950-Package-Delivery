import csv
from package import Package
from hash_table import HashTable
from truck import Truck

wgu_packages = HashTable()  # Initialize Hash Table


# Initialize trucks and fill with packages and return trucks O(n)
def initialize():

    filename = "WGUPS Package File final.csv"

    # Initialize Trucks
    trucks = [Truck("8:00:00"), Truck("9:10:00"), Truck("11:00:00")]

    # Read CSV File
    with open(filename, 'r') as package_data_file:
        package_data = csv.reader(package_data_file, delimiter=",")

        # Loop through each line in CSV file to create package list O(n)
        for line in package_data:

            # Create new package object
            new_package = Package(int(line[0]), line[1], line[2], line[3], line[4], line[5], line[6], line[7])

            # Insert Key/Value pairs into the hash table
            wgu_packages.insert(new_package.id, new_package)

            # Statements to determine which truck each package will be added to O(n)

            # Find package with wrong address to make sure package leaves facility after corrected
            if new_package.notes == "Wrong address listed":
                trucks[2].add_item(new_package)
                new_package.start = trucks[2].leave_time.time()

            # List for first trucks delivery. Prioritized based upon delivery deadline
            if new_package.delivery_time != "EOD" or new_package.id == 19:
                if len(new_package.notes) < 1 or "Must" in new_package.notes:
                    trucks[0].add_item(new_package)
                    new_package.start = trucks[0].leave_time.time()

            # List for packages that must be in the second truck or was delayed with a delivery deadline
            if "Delayed" in new_package.notes or "Can only" in new_package.notes:
                trucks[1].add_item(new_package)
                new_package.start = trucks[1].leave_time.time()

            # Place remaining packages in second or third truck depending on which has more packages
            if (new_package not in trucks[0].items and
                    new_package not in trucks[1].items and
                    new_package not in trucks[2].items):

                if len(trucks[1].items) < len(trucks[2].items):
                    trucks[1].add_item(new_package)
                    new_package.start = trucks[1].leave_time.time()
                else:
                    trucks[2].add_item(new_package)
                    new_package.start = trucks[2].leave_time.time()
    return trucks

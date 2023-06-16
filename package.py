# Class to store package information O(1)

class Package:
    def __init__(self, id, address, city, state, zip, delivery_time, weight, notes):
        # Initialize the Package with each package variable
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_time = delivery_time
        self.weight = weight
        self.notes = notes
        self.status = "At Hub"
        self.start = ""
        self.location = ""

    # Function to print each component of the package
    def print(self):
        print("ID: ", self.id,", Address: ", self.address, " ", self.city, " ", self.state, ", ", self.zip,", Weight: ", self.weight,
              ", Notes: ", self.notes, ", Leave Time: ", self.start, self.location, ", Status: ", self.status,
              ", Delivery Time: ", self.delivery_time, sep='')

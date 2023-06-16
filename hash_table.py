# Class for hash table to store and retrieve all package information O(1)

class HashTable:
    # Initialize hash table with empty list
    def __init__(self, initial_capacity=41):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts value into hash table
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(value)

    # Searches for value based on key and returns value, or None if not found
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        return bucket_list

    # Removes a value with matching key from the hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)

# Chapter 7 Section 8 of C950: Data Structures and Algorithms II
# I used the chaining hash table example to help create my hash table

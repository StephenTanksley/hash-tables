class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        # Need to use HashTableEntry to populate a hash table with new capacity


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if (capacity >= MIN_CAPACITY):
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        # Using the pre-determined capacity to determine how large the table is.
        self.table = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        # We return the length of the array that we've initialized.
        return len(self.table)

    def get_load_factor(self):
        """
        Naive implementation - just loop through the table to make sure that you're getting all items. 

        """
        # This is a naive implementation which assumes that only one item is present at any one location.
        # loaded_table = [item != None for item in self.table]
        # load_factor = len(loaded_table) / self.capacity
        # return load_factor

        """
        PROBLEM: How do we handle the case where more than one item may already exist at that index?
        
        SOLUTION: We need to set up logic to handle the case where there may be a linked list chain.
        
            Pre-loop - set up a counter. Counter = 0
            1) Set up a loop to cycle through items in the table. We'll want to keep track of the current node.
                1a) If the current item (first item in the loop) has value, we want to increment counter += 1. 
                1b) We're really only interested in checking things if they have value.
            2) while current_node.next is not None:
                2a) If i.next has value, increment counter += 1.
                2b) Move to next node. current_node = current_node.next
                2c) If current_node.next is None, we can return and move to the next item in the table and repeat.
            3) Divide counter / capacity. This is going to account for items which may have been hashed into the same spot.
        """

        counter = 0

        # Need to ask Hui about this. Not sure the BigO properties here. Normally I'd say O(n) judging by the length of the list, but we also have to consider that by using a linked list, we're potentially overloading each slot.

        for i in self.table:
            current_node = i
            if current_node.value is not None:
                counter += 1
                while current_node.next is not None:
                    current_node = current_node.next

        return counter / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)

        # hash_value = ((5381 * 2^5) + 5381) + ord(x)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Under the hood, this is converting the provided key to a hash and then reducing it to an index.
        hashed_key = self.hash_index(key)

        # This creates a new entry into the table will be the head of a Linked List.
        new_entry = HashTableEntry(key, value)

        # If there's nothing at the location, insert the new entry there.
        if self.table[hashed_key] == None:
            self.table[hashed_key] = new_entry
        # If there IS something at that location, we should chain onto it.
        else:
            # Theoretically, this should be creating the pointer reference to the current "head" and then overwriting it with the new data.
            new_entry.next = self.table[hashed_key]
            self.table[hashed_key] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_key = self.hash_index(key)
        data = self.table[self.hash_index(key)]

        if data:
            self.table[hashed_key] = None
        else:
            return f'Item at index {hashed_key} was not found.'

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_index = self.hash_index(key)
        data = self.table[hashed_index]
        if data:
            return data
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("Current load factor: ", ht.get_load_factor())

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

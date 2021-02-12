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
    A hash table that with `capacity` table
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
        # self.load_factor = None -- Used for a slower implementation.
        self.items = 0

    def get_num_slots(self):

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

        # counter = 0

        # # Need to ask Hui about this. Not sure the BigO properties here. Normally I'd say O(n) judging by the length of the list, but we also have to consider that by using a linked list, we're potentially overloading each slot.

        # for i in self.table:
        #     current_node = i
        #     if current_node.value is not None:
        #         counter += 1
        #         while current_node.next is not None:
        #             current_node = current_node.next

        # self.load_factor = counter / self.capacity

        # return self.load_factor
        load_factor = self.items / self.capacity
        return load_factor

    def fnv1(self, key):

        pass

    def djb2(self, key):

        # Your code here
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)

        # hash_value = ((5381 * 2^5) + 5381) + ord(x)
        return hash & 0xffffffff

    def hash_index(self, key):

        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):

        new_entry = HashTableEntry(key, value)
        hashed_index = self.hash_index(key)

        # Find the place to start the insertion.
        if self.table[hashed_index] is not None:

            # If something already exists there...
            current = self.table[hashed_index]
            while current is not None:
                # if the key already exists
                if current.key == key:
                    # overwrite what's there currently. We no longer need what was there before.
                    current.value = value
                    return
                current = current.next
            # add the new_entry to the head of the linked list.
            current_head = self.table[hashed_index]
            self.table[hashed_index] = new_entry
            self.table[hashed_index].next = current_head
            self.items += 1

        # If we get lucky and there's nothing in the spot at the hashed index.
        else:
            # add new_entry
            self.table[hashed_index] = new_entry
            self.items += 1

        # automatic resizing if load factor increases above 0.7
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):

        # hash the current key to get the index for the table.
        hashed_index = self.hash_index(key)

        # If the table has an entry at that index
        if self.table[hashed_index] is not None:

            # set the current node to be the head of that list
            current = self.table[hashed_index]

            # if we get lucky and the current key is the one we're looking for
            if current.key == key:
                # change our currently selected index to point to next thing in the list.
                self.table[hashed_index] = current.next
                # reduce the number of items that we're tracking by one.
                self.items -= 1
                return current.value

            # Otherwise, we want to keep track of what the previous value was because we'll have to cut out the linked list node we're evaluating and link around it.
            previous = current
            current = current.next

            # We repeat the process of checking the key down the line
            while current is not None:
                if current.key == key:
                    previous.next = current.next
                    self.items -= 1
                    return current.value
                else:
                    previous = current
                    current = current.next

        # Finally, check to make sure that we're in our parameters for the load_factor.
        if self.get_load_factor() < 0.2:
            self.resize(self.capacity // 2)

        return f"Key at table index {hashed_index} was not found."

    def get(self, key):
        # Your code here
        hashed_index = self.hash_index(key)

        current = self.table[hashed_index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # create a reference to the old table.
        old_table = self.table

        # define the new capacity for the table.
        self.capacity = new_capacity if new_capacity >= MIN_CAPACITY else MIN_CAPACITY

        # create a new table at the new capacity.
        new_table = [None] * self.capacity
        self.table = new_table

        # reset items to 0
        self.items = 0

        for entry in old_table:
            current_entry = entry

            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next


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

import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None
        self.prev_node = None

class ResizableHashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.buckets = [None] * self.size

    def compute_index(self, key):
        # Using multiplication and division methods
        phi = (1 + math.sqrt(5)) / 2  # Golden ratio
        temp = key * phi
        fractional = temp - int(temp)
        index = int(self.size * fractional)
        return index % self.size

    def resize(self, new_size):
        new_buckets = [None] * new_size
        for bucket in self.buckets:
            current = bucket
            while current:
                next_node = current.next_node
                new_index = self.compute_index(current.key)
                current.next_node = new_buckets[new_index]
                current.prev_node = None
                if new_buckets[new_index]:
                    new_buckets[new_index].prev_node = current
                new_buckets[new_index] = current
                current = next_node
        self.buckets = new_buckets
        self.size = new_size

    def add_item(self, key, value):
        if self.count >= self.size:
            self.resize(self.size * 2)

        index = self.compute_index(key)
        new_node = Node(key, value)
        new_node.next_node = self.buckets[index]
        if self.buckets[index]:
            self.buckets[index].prev_node = new_node
        self.buckets[index] = new_node
        self.count += 1

    def delete_item(self, key):
        index = self.compute_index(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.buckets[index] = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                self.count -= 1

                if self.count <= self.size // 4 and self.size > 8:
                    self.resize(self.size // 2)
                return
            current = current.next_node

    def get_value(self, key):
        index = self.compute_index(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next_node
        return None  # Key not found

    def total_items(self):
        return self.count

    def current_size(self):
        return self.size

# Test the ResizableHashTable
if __name__ == "__main__":
    hash_table = ResizableHashTable()

    # Insert some key-value pairs
    hash_table.add_item(7, 70)
    hash_table.add_item(17, 170)
    hash_table.add_item(27, 270)

    # Retrieve and print values
    print(f"Value for key 7: {hash_table.get_value(7)}")
    print(f"Value for key 17: {hash_table.get_value(17)}")
    print(f"Value for key 27: {hash_table.get_value(27)}")

    # Remove a key
    hash_table.delete_item(17)

    # Try to retrieve the removed key
    print(f"Value for key 17 after removal: {hash_table.get_value(17)}")

    # Insert many items to test resizing
    for i in range(100):
        hash_table.add_item(i, i * 10)

    print(f"Final item count: {hash_table.total_items()}")
    print(f"Final container size: {hash_table.current_size()}")
"""OUTPUT
Value for key 7: 70
Value for key 17: 170
Value for key 27: 270
Value for key 17 after removal: None
Final item count: 102
Final container size: 128
"""
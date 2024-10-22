This project implements a dynamic hash table that grows and shrinks as needed, using integer keys and values. The hash function combines multiplication and division methods, multiplying the key by the golden ratio and using modulo to compute the index. Collisions are handled via chaining with a doubly linked list, where each bucket can hold multiple items.

Key operations include inserting, removing, and retrieving key-value pairs. The table resizes dynamically: it doubles when full and halves when one-fourth empty, rehashing all items during resizing. The main components are DualNode for key-value pairs and DynamicHashStructure for managing the hash table. This provides efficient insertion, deletion, and retrieval with automatic resizing for optimal performance.

Output
Value for key 7: 70
Value for key 17: 170
Value for key 27: 270
Value for key 17 after removal: None
Final item count: 102
Final container size: 128

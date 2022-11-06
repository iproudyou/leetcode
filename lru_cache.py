"""
    The idea is to have a dictionary store keys and values
    while having a doubly linked list to keep track of LRU.
"""
from collections import defaultdict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.front = None
        self.back = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = defaultdict()
        self.doubly_linked_list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.dict:
            self._remove(self.dict[key])
            self._insert_back(self.dict[key])
            return self.dict[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        n = Node(key, value)

        # if the capacity exceeds
        if key not in self.dict:
            exceed_capacity = len(self.dict) >= self.capacity
            front_node = self.doubly_linked_list.front

            if exceed_capacity and front_node:
                self.dict.pop(front_node.key)
                self._remove(front_node)

        # remove from the doubly linked list
        else:
            self._remove(self.dict[key])

        # insert or update
        self._insert_back(n)
        self.dict[key] = n
    
    def _insert_back(self, node: Node):
        """inserts to the back of the doubly linked list"""
        if not self.doubly_linked_list.front and not self.doubly_linked_list.back:
            self.doubly_linked_list.front = node
            self.doubly_linked_list.back = node
        else:
            self.doubly_linked_list.back.next = node
            node.prev = self.doubly_linked_list.back
            node.next = None

            self.doubly_linked_list.back = node

    def _remove(self, node: Node):
        """removes the node"""
        if node.prev is None and node.next is None:
            self.doubly_linked_list.front = None
            self.doubly_linked_list.back = None

        elif node.prev is None:
            self.doubly_linked_list.front = node.next 
            node.next.prev = None

        elif node.next is None:
            self.doubly_linked_list.back = node.prev 
            node.prev.next = None
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            
lru_cache = LRUCache(2)
lru_cache.put(1, 1) 
lru_cache.put(2, 2)
print(lru_cache.get(1))
lru_cache.put(3, 3)
print(lru_cache.get(2))
lru_cache.put(4, 4)
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))

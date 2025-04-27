class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_node(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        # NOTE: important to clear its pointers to others, as this may cause cycles
        self.next, self.prev = None, None
        return self

    def append_node(self, new_node):
        if self.next is not None:
            self.next.prev = new_node
            new_node.next = self.next
        self.next = new_node
        new_node.prev = self
    

class LRUCache:
    def __init__(self, capacity: int):
        self._map = {}
        self._head = DLinkedNode()
        self._tail = DLinkedNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self.capacity = capacity

    def _move_to_end(self, node: DLinkedNode) -> None:
        removed = node.remove_node()
        self._tail.prev.append_node(removed)
        self._tail.prev = removed

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        self._move_to_end(self._map[key])
        return self._map[key].value

    def put(self, key: int, value: int) -> None:
        node = (
            self._map[key]
            if key in self._map 
            else DLinkedNode(key=key, value=value)
        )
        node.value = value
        self._move_to_end(node)
        self._map[key] = node

        if len(self._map) > self.capacity:
            removed = self._head.next.remove_node()
            del self._map[removed.key]



def test_lru_cache():
    l = LRUCache(2)
    l.put(1,1)
    l.put(2,2)
    v = l.get(1)
    assert v == 1, v
    l.put(3,3)
    assert l.get(2) == -1
    l.put(4,4)
    assert l.get(1) == -1
    assert l.get(3) == 3
    assert l.get(4) == 4

    l = LRUCache(1)
    l.put(2,1)
    assert l.get(2) == 1
    l.put(3,2)
    assert l.get(2) == -1
    assert l.get(3) == 2

    l = LRUCache(2)
    l.put(2,1)
    l.put(2,2)
    assert l.get(2) == 2
    l.put(1,1)
    l.put(4,1)
    l.get(2) == -1

test_lru_cache()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

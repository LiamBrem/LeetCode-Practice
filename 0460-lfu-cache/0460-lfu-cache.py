class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)  # sentinel
        self.tail = Node(0, 0)  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.node_map = {}          # key -> node
        self.freq_map = defaultdict(DLL)  # freq -> DLL

    def _update(self, node):
        f = node.freq
        self.freq_map[f].remove(node)
        if self.freq_map[f].size == 0 and f == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        self._update(self.node_map[key])
        return self.node_map[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_map:
            self.node_map[key].val = value
            self._update(self.node_map[key])
        else:
            if len(self.node_map) == self.capacity:
                evicted = self.freq_map[self.min_freq].remove_tail()
                del self.node_map[evicted.key]
            node = Node(key, value)
            self.node_map[key] = node
            self.freq_map[1].add_to_head(node)
            self.min_freq = 1
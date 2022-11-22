class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.queue = list()
        self.data = {}

    def put(self, key, value):
        self.data[key] = value
        if len(self.data) >= self.capacity:
            if key in self.queue:
                self.queue.remove(key)
            else:
                del self.data[self.queue.pop()]
        self.queue.insert(0, key)

    def get(self, key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.insert(0, key)
        return self.data.get(key)

from collections import OrderedDict
class LRUCache:
    #O(1) for every addition as well as O(n) because we are storing at n nodes of capacity
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        # we check first if we are at limit 
        elif len(self.cache)>=self.capacity:
            #pop the first item
            self.cache.popitem(last=False)
        # we add new value in cache
        self.cache[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
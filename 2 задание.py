# 2 задание
class LRUCache:
    def __init__(self, capacity):
        self._cache = {}
        self.capacity = capacity
        self.old_elem = 0
        self.val = ()
        self.new_elem = 0
        self.lru_items = {}

    @property
    def cache(self):
        return self.old_elem

    @cache.setter
    def cache(self, new_elem):
        self.new_elem = new_elem
        self._cache[self.new_elem[0]] = self.new_elem[1]
        l = list(self._cache.keys())
        if len(l) > 0:
            self.old_elem = l[0]
        if len(self._cache) > self.capacity:
            del self._cache[self.old_elem]

    def get(self, key):
        if len(self._cache) > 0:
            self.val = self._cache[key]
            del self._cache[key]
            self._cache[key] = self.val
            return self._cache.get(key)

    def print_cache(self):
        if len(self._cache) > 0:
            self.lru_items = self._cache.items()
        print("\nLRU Cache:")
        for key, value in self._cache.items():
            print(f'{key} : {value}')
        print('')


cache = LRUCache(3)
cache.cache = ('key1', 'value1')
cache.cache = ('key2', 'value2')
cache.cache = ('key3', 'value3')
cache.print_cache()
print(cache.get('key2'))
cache.cache = ('key4', 'value4')
cache.print_cache()

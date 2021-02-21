class MyHashSet(object):
    keys = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = [0] * 1000001

    def add(self, key):
        self.keys[key] = 1

    def remove(self, key):
        self.keys[key] = 0

    def contains(self, key):
        return self.keys[key] == 1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
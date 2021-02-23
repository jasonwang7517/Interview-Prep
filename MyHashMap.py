class MyHashMap(object):
    keys = []

    def __init__(self):
        self.keys = [-1] * 1000001

    def put(self, key, value):
        self.keys[key] = value

    def get(self, key):
        return self.keys[key]

    def remove(self, key):
        self.keys[key] = -1

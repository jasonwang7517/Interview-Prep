"""
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:
    - void add(key) Inserts the value key into the HashSet.
    - bool contains(key) Returns whether the value key exists in the HashSet or not.
    - void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

class MyHashSet(object):
    keys = []

    def __init__(self):
        self.keys = [0] * 1000001

    def add(self, key):
        self.keys[key] = 1

    def remove(self, key):
        self.keys[key] = 0

    def contains(self, key):
        return self.keys[key] == 1
class OrderedStream(object):
    arr = []
    ptr = 0

    def __init__(self, n):
        self.arr = [""] * n
        

    def insert(self, id, value):
        self.arr[id - 1] = value
        l = []
        for i in range (self.ptr, len(self.arr)):
            if self.arr[i] == "":
                break
            else:
                l.append(self.arr[i])
                self.ptr += 1
        return l
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
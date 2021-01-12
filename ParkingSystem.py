class ParkingSystem(object):
    arr = [0] * 3

    def __init__(self, big, medium, small):
        self.arr[0] = big
        self.arr[1] = medium
        self.arr[2] = small

    def addCar(self, carType):
        self.arr[carType - 1] -= 1
        return (self.arr[carType - 1]) >= 0
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
class Bus:
    """Bus is a generic class for the vehicles of type Bus"""
    def __init__(self, busType, capacity=30):
        self.busType = busType
        self.capacity = capacity
    
    def move(self, fromLocation, toLocation):
        print(f'Bus of type {self.busType} with capacity {self.capacity} is going from {fromLocation} to {toLocation}')
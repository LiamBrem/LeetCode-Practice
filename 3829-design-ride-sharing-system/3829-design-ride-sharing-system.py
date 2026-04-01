"""
- queue for riders & drivers -> pop at front/end
- for faster cencellations -> set w/ inactive riders
- when popping -> if inactive skip

- however, if we have a long queue, and all get canceled -> will have to pop all of them

- could implement a doubly linked list with a dict pointing the id: node -> remove node when id becomes inactive O(1)
"""

class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.allRiders = set()
        self.drivers = deque()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.allRiders.add(riderId)
        
    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.riders or not self.drivers:
            return [-1, -1]

        while self.riders:
            riderId = self.riders.popleft()
            if riderId in self.allRiders:
                driverId = self.drivers.popleft()
                self.allRiders.remove(riderId)
                return [driverId, riderId]

        return [-1, -1] 
        

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.allRiders:
            self.allRiders.remove(riderId)
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
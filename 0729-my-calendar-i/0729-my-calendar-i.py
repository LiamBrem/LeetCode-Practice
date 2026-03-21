class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.bookings) - 1

        for start, end in self.bookings:
            if not (endTime <= start or startTime >= end):
                return False
                
        self.bookings.append((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
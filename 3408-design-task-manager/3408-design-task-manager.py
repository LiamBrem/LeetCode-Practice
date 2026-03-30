"""
priroty queue:
- add = O(logn)
- edit = O(n)
- rmv = O(n)
- execTop = O(logn)


"""
import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]): # [userId, taskId, priority]
        self.pq = []
        self.d = {}

        for userId, taskId, priority in tasks:
            self.d[taskId] = (priority, userId)
            self.pq.append((-priority, -taskId, userId))

        heapq.heapify(self.pq)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.pq, (-priority, -taskId, userId))
        self.d[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.d[taskId][1]
        self.d[taskId] = (newPriority, userId)

        heapq.heappush(self.pq, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        del self.d[taskId]

    def execTop(self) -> int:
        while self.pq:
            priority, taskId, userId = heapq.heappop(self.pq)
            taskId = -taskId
            priority = -priority

            if taskId in self.d and self.d[taskId] == (priority, userId):
                del self.d[taskId]
                return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
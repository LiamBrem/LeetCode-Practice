"""
map {parent: [child, child]}
map {node: locked/unlocked}


"""
from collections import defaultdict, deque
class LockingTree:
    def p(self):
        print("----------------------------")
        print("isunlocked:", self.isUnlocked)
        print("children:", self.children)
        print("parents:", self.parents)

    def __init__(self, parent: List[int]):
        self.isUnlocked = {} # {node: (bool, user)}
        self.children = defaultdict(list) # {parent: [child, child, child]}
        self.parents = {} # {child: parent}

        for i, p in enumerate(parent):
            self.children[p].append(i)
            self.parents[i] = p
            self.isUnlocked[i] = [True, None]

        # self.p()

    def lock(self, num: int, user: int) -> bool:
        if self.isUnlocked[num][0]:
            self.isUnlocked[num][0] = False
            self.isUnlocked[num][1] = user
            # self.p()
            return True
        else:
            # self.p()
            return False

    def unlock(self, num: int, user: int) -> bool:
        isUnlocked, username = self.isUnlocked[num]
        if isUnlocked:
            # self.p()
            return False
        elif user == username or user == "admin":
            self.isUnlocked[num][0] = True
            self.isUnlocked[num][1] = None
            # self.p()
            return True
        else:
            # self.p()
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        # make sure no ancestors are locked
        curr = num
        while curr != -1:
            if self.isUnlocked[curr][0] == False:
                # self.p()
                return False

            curr = self.parents[curr]

        toUnlock = []
        atLeastOneLocked = False
        q = deque()
        q.append(num)
        while q:
            curr = q.popleft()
            if self.isUnlocked[curr][0] == False: # locked
                atLeastOneLocked = True
                toUnlock.append(curr)
            for nxt in self.children[curr]:
                q.append(nxt)

        if atLeastOneLocked == False:
            # self.p()
            return False
        else:
            for numToUnlock in toUnlock:
                # print(1, self.unlock(numToUnlock, "admin"))
                self.unlock(numToUnlock, "admin")

            # print(2, self.lock(num, user))
            self.lock(num, user)
            # self.p()
            return True
            


        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
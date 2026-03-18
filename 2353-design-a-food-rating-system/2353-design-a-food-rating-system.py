class PQ:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.indexes = {} # {food: index}

    def heapify_down(self, i):
        n = self.size
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
    
            def better(a, b):
                if a[0] != b[0]:
                    return a[0] > b[0]
                return a[1] < b[1]
    
            if left < n and better(self.arr[left], self.arr[largest]):
                largest = left
    
            if right < n and better(self.arr[right], self.arr[largest]):
                largest = right
    
            if largest == i:
                break
    
            self.indexes[self.arr[i][1]] = largest
            self.indexes[self.arr[largest][1]] = i
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]

            i = largest


    def heapify_up(self, i):
        def better(a, b):
            if a[0] != b[0]:
                return a[0] > b[0]
            return a[1] < b[1]
    
        while i > 0:
            parent = (i - 1) // 2
            if better(self.arr[i], self.arr[parent]):
                self.indexes[self.arr[i][1]] = parent
                self.indexes[self.arr[parent][1]] = i
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break


    def addFood(self, food, rating):
        self.arr.append((rating, food))
        i = self.size
        self.size += 1
        self.indexes[food] = i
        self.heapify_up(i)



    def updateFood(self, food, rating):
        i = self.indexes[food]
        old = self.arr[i]
        self.arr[i] = (rating, food)
        if rating > old[0] or (rating == old[0] and food < old[1]):
            self.heapify_up(i)
        else:
            self.heapify_down(i)

       

    def peek(self):
        return self.arr[0][1]


class FoodRatings:
    """
    foods[i] == cuisines[i] == ratings[i]
    foods = names
    cuisines = type
    ratings = initial rating

    hashmap {cuisine: [pq of foods]}
    pq can be indexable so that we have O(logn) updates (as opposed to O(n))
    O(1) to get highestRated
    """
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.m = {}
        self.food_to_cuisine = defaultdict(str)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.m:
                self.m[cuisine] = PQ()
            self.m[cuisine].addFood(food, rating)

            self.food_to_cuisine[food] = cuisine


    def changeRating(self, food: str, newRating: int) -> None: # changes rating of food
        cuisine = self.food_to_cuisine[food]
        self.m[cuisine].updateFood(food, newRating)

    def highestRated(self, cuisine: str) -> str: # highest rated food of type cuisine
        return self.m[cuisine].peek()
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
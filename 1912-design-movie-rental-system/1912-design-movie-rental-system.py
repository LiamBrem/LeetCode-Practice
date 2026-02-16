class MovieRentingSystem:
    # at most 1 copy of movie per shop
    # movie at shop of price
    def __init__(self, n: int, entries: List[List[int]]): # [shop, movie, price]
        self.price = {} # {(shop, movie): price}
        self.available = defaultdict(list) # movie: min heap sorted by (price, shop)
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            heapq.heappush(self.available[movie], (price, shop))
        
        self.rented = [] # min heap sorted by (price, shop, movie)
        self.rented_set = set() # {(shop, movie)}


    # cheapest 5 shops that have an unrented copy of movie
    # sorted by price in ascending order
    # tie -> smaller shopi appears first
    def search(self, movie: int) -> List[int]:
        res = []
        temp = []
        # seen = set()

        while self.available[movie] and len(res) < 5:
            price, shop = heapq.heappop(self.available[movie])
            temp.append((price, shop))

            if (shop, movie) not in self.rented_set:
                # seen.add(shop)
                res.append(shop)

        for t in temp:
            heapq.heappush(self.available[movie], t)
        
        return res


    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        price = self.price[(shop, movie)]
        heapq.heappush(self.rented, (price, shop, movie))

    # return
    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.remove((shop, movie))
        

    # 5 cheapest rented movies -> [shop, movie]
    # sorted by price in ascending order
    # tie smaller shop; tie smaller movie
    def report(self) -> List[List[int]]:
        res = []
        temp = []
        seen = set()

        while self.rented and len(res) < 5:
            price, shop, movie = heapq.heappop(self.rented)

            if (shop, movie) in self.rented_set:
                temp.append((price, shop, movie))

                if (shop, movie) not in seen:
                    seen.add((shop, movie))
                    res.append([shop, movie])

        for t in temp:
            heapq.heappush(self.rented, t)

        return res
            
       


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
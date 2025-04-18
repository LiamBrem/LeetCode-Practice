class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            new = 0
            while n >= 1:
                new += (n % 10)**2
                n //= 10
            n = new
            print(n)

        if n == 1:
            return True
        elif n in seen:
            return False
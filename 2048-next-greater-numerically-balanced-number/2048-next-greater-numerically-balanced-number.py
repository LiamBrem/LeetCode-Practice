class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isOccuring(n):
            s = str(n)
            c = Counter(s)
            for key in c.keys():
                if c[key] != int(key):
                    return False

            return True

        n += 1
        while True:
            if isOccuring(n):
                return n
            n += 1


class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary
        
    def numberOfDifferences(self, word: str, searchWord: str) -> int:
        total = 0
        for i in range(len(word)):
            if word[i] != searchWord[i]:
                total += 1

        return total

    def search(self, searchWord: str) -> bool:
        for word in self.dictionary:
            if len(word) == len(searchWord) and self.numberOfDifferences(word, searchWord) == 1:
                return True


        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
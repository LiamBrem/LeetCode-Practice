"""
- Can simulate with a string or array
- get's inefficient when we call addTex + cursorLeft many times
- (has to shift all elements each time or string is copying)
- would be the simplest solution - especially for curxor left and right w/ slicing

- another option could be a dict {pos: [c,c,c,c,c,]}
- where pos could increment by 10 and c represents a character
- however, that would make accessing for operations more difficult
    - access dict at nearest 10, plus shifting elements between - would have to shift every element anyway to left or right

- we could use a stack (left and right)
- where the top of left stack is the first char to the left & vice versa o(k)
- addText would all have to be appended to left stack O(k)
- delete removes from the left stack 0(1)
- cursor left/right just switches elements between the stacks O(1)


"""
class TextEditor:

    def __init__(self):
        self.ls = []
        self.rs = []
       
    def addText(self, text: str) -> None:
        for i in range(len(text)):
            self.ls.append(text[i])


    def deleteText(self, k: int) -> int:
        total = 0
        for i in range(k):
            if self.ls:
                self.ls.pop()
                total += 1
            else:
                break

        return total

    def getLastTen(self) -> str:
        res = ""
        for i in range(min(10, len(self.ls))):
            res += self.ls[-(i + 1)]

        return res[::-1]

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if self.ls:
                self.rs.append(self.ls.pop())
        
        return self.getLastTen()
        

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if self.rs:
                self.ls.append(self.rs.pop())

        
        return self.getLastTen()

        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
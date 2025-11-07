class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "[":"]", "{": "}"}

        for val in s:
            if len(stack) <= 0:
                if val in pairs:
                    stack.append(val)
                else:
                    return False
            else:
                if val not in pairs:
                    lastElem = stack.pop()
                    if pairs[lastElem] != val:
                        return False
                else:
                    stack.append(val)
                    
        return len(stack) == 0


        
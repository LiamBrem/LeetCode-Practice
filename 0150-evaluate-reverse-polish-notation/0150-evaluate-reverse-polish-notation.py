class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token.isdigit():
                s.append(int(token))
            elif token[0] == "-" and len(token) > 1:
                s.append(-int(token[1:]))
            else:
                v1 = s.pop()
                v2 = s.pop()
                if token == "+":
                    s.append(v2 + v1)
                elif token == "-":
                    s.append(v2 - v1)
                elif token == "*":
                    s.append(v2 * v1)
                else:
                    s.append(int(v2 / v1))
                
        
        return s[0]
        
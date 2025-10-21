"""
input: string (unsimplified path)
output: string (simplified canonical path)

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        vals = path.split("/")

        for val in vals:
            if val == '' or val == '.':
                continue
            elif val == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(val)


        res = ""
        for val in stack:
            res += "/" + val

        if not res:
            res = "/"

        return res

        
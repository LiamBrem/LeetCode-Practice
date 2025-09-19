'''
input: list of strings of subfolders
output: list of strings of subfolders after removal

notes:
- 

'''

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        print(folder)
        res = []

        for item in folder:
            if len(res) == 0:
                res.append(item)

            else:
                prev = res[-1]
                if len(item) > len(prev) and item.startswith(prev) and item[len(prev)] == "/":
                    continue
                else:
                    res.append(item)

        return res

        
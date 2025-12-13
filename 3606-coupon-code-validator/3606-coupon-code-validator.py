class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        d = defaultdict(list)

        for i in range(len(code)):
            if len(code[i]) > 0 and all(ch.isalnum() or ch == "_" for ch in code[i]) and isActive[i]:
                if businessLine[i] == "electronics":
                    d["electronics"].append(code[i])

                elif businessLine[i] == "grocery":
                    d["grocery"].append(code[i])

                elif businessLine[i] == "pharmacy":
                    d["pharmacy"].append(code[i])

                elif businessLine[i] == "restaurant":
                    d["restaurant"].append(code[i])

        res = []
        for word in ("electronics", "grocery", "pharmacy", "restaurant"):
            if len(d[word]) > 0:
                res += (sorted(d[word]))

        return res

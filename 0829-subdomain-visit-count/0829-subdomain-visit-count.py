class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for cpdomain in cpdomains:
            sections = cpdomain.split()
            count = int(sections[0])

            domain = sections[1]

            while domain:
                if domain in d:
                    d[domain] += count
                else:
                    d[domain] = count

                if "." in domain:
                    pIndex = domain.index(".")
                    domain = domain[pIndex + 1:]
                else:
                    domain = ""

        result = []
        for key in d:
            result.append(str(d[key]) + " " + key)

        return result
            
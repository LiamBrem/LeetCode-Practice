from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        # build hash map of subdomain: count
        hMap = defaultdict(int)

        # loop through cpdomains
        for string in cpdomains:
            # separate string into int then domain
            [count, domain] = string.split(" ")
            count = int(count)
            
            # for each domain, while string isn't empty, add totals
            while "." in domain:
                hMap[domain] += count

                # remove domain up until . 
                dotPosition = domain.index(".")

                # edge case: check if dot exists
                domain = domain[dotPosition + 1:]

            hMap[domain] += count

        result = []

        for value in hMap:
            result.append(f"{str(hMap[value])} {value}")


        return result

        
        
        
        
        
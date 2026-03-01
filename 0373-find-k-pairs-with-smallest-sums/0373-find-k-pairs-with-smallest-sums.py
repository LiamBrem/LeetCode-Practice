class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen = set()
        res = []
        pq = []

        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))

        while pq and len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(pq, (nums2[j + 1] + nums1[i], i, j + 1))


        return res
                
        
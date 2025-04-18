class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        rows, cols = len(matrix), len(matrix[0])

        arr = []

        if len(matrix) == 1:
            arr = matrix[0]

        else:

            while l <= r:
                mid = (l + r) // 2

                if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                    arr = matrix[mid]
                    break
                elif matrix[mid][0] < target:
                    l = mid + 1
                elif matrix[mid][0] > target:
                    r = mid - 1

        if not arr:
            return False


        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid -1


        return False
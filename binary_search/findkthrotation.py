class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1
        min_val = float("inf")
        min_idx = -1

        while low <= high:
            mid = (low + high) // 2

            # left half sorted
            if arr[low] <= arr[mid]:
                if arr[low] < min_val:
                    min_val = arr[low]
                    min_idx = low
                low = mid + 1
            else:
                if arr[mid] < min_val:
                    min_val = arr[mid]
                    min_idx = mid
                high = mid - 1

        return min_idx

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


if __name__ == "__main__":
    s = Solution()
    tests = [
        [15, 18, 2, 3, 6, 12],
        [7, 9, 11, 12, 5],
        [1, 2, 3, 4, 5],
        [],
    ]
    for arr in tests:
        print(arr, "-> rotation index:", s.findKRotation(arr))

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find in which half the target is present in first half or second half
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([], 1, -1),
        ([1], 1, 0),
    ]

    for arr, target, expected in tests:
        arr_copy = list(arr)
        try:
            out = sol.search(arr_copy, target)
        except Exception as e:
            out = f"ERROR: {e}"
        status = "PASS" if out == expected else "FAIL"
        print(
            f"input: {arr} target: {target} -> output: {out} | expected: {expected} => {status}"
        )

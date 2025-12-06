from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        newarr = [0] * len(nums)
        odd = 1
        even = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                newarr[even] = nums[i]
                even = even + 2
            else:
                newarr[odd] = nums[i]
                odd = odd + 2
        return newarr


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [3, 1, -2, -5, 2, -4],
        [-1, 1, -2, 2, -3, 3],
        [2, -1],
        [1, -1, 1, -1, 1, -1],
        [],  # empty
    ]

    for nums in tests:
        try:
            out = sol.rearrangeArray(nums)
        except Exception as e:
            out = f"ERROR: {e}"
        print(f"input: {nums} -> output: {out}")

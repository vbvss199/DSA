from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float("-inf")
        sum = 0
        start = 0
        arrStart = 0
        arrEnd = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if sum == 0:
                start = i
            if sum > max:
                max = sum
                arrStart = start
                arrEnd = i
            if sum < 0:
                sum = 0
                start = i + 1
        k = nums[arrStart : arrEnd + 1]
        return max


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # expected 6
        [-1, -2, -3, -4],  # expected -1
        [-5],  # expected -5
        [-2, -3, -1, -4, -1],  # expected -1
        [1, 2, 3, -2, 5],  # expected 9
        [0, -1, 0, -2, 0],  # expected 0
        [-2, -1, -2, -3, -1, -4],  # expected -1
        [10, -3, -4, 7, 6, 5, -2, -1],  # mixed positives/negatives
    ]

    for arr in tests:
        print(f"{arr} -> {sol.maxSubArray(arr)}")

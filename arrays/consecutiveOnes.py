from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
    ]
    for test in tests:
        print(f"{test}->{sol.findMaxConsecutiveOnes(test)}")

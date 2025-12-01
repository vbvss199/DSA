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
        [],  # empty array
        [1, 1, 1, 1, 1],  # all ones
        [0, 0, 0, 0],  # all zeros
        [1],  # single one
        [0],  # single zero
        [1, 0, 1, 0, 1, 0, 1],  # alternating
        [0, 1, 1, 1, 0, 1, 1],  # multiple runs
        [1] * 20 + [0] + [1] * 5,  # long run then shorter run
    ]
    for test in tests:
        print(f"{test}->{sol.findMaxConsecutiveOnes(test)}")

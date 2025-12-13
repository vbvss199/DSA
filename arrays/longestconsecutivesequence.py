from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqMap = {}
        currentcount = 0
        maxcount = float("-inf")
        currentElement = nums[0]
        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1
        for x in freqMap:
            if x - 1 not in freqMap:
                currentcount = 1
                currentElement = x
                while currentElement + 1 in freqMap:
                    currentcount = currentcount + 1
                    currentElement = currentElement + 1
                maxcount = max(currentcount, maxcount)
        return maxcount


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),  # 1,2,3,4
        ([2, 2, 2], 1),
        ([1, 2, 2, 3], 3),  # 1,2,3
        ([0, -1, 1], 3),  # -1,0,1
        ([-3, -2, -1, 0, 1], 5),  # -3..1
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),  # 3..9 or -1..1 etc (expected 7)
        ([1, 3, 5, 7, 9], 1),  # no consecutive neighbors
        ([10, 11, 12, 5, 6, 7, 8], 4),  # 5..8 or 10..12 -> 4
    ]

    for nums, expected in tests:
        try:
            out = sol.longestConsecutive(list(nums))
        except Exception as e:
            out = f"ERROR: {e}"
        status = "PASS" if out == expected else "FAIL"
        print(
            f"input: {nums[:20]}{'...' if len(nums)>20 else ''} -> output: {out} | expected: {expected} => {status}"
        )

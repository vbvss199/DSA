from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1

        sorted_array = sorted(mpp.items(), key=lambda x: x[1], reverse=True)
        max_freq = max(mpp.values())
        count = 0
        for freq in mpp.values():
            if freq == max_freq:
                count = count + freq

        return count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1, 2, 2, 3, 3, 3],  # 3 appears 3 times -> count = 3
        [4, 4, 5, 5],  # 4 and 5 each appear 2 times -> count = 4 (2+2)
        [7, 7, 7, 7],  # single value -> 4
        [1, 2, 3, 4, 5],
    ]
    for test in tests:
        print(f"{test}->{sol.maxFrequencyElements(test)}")

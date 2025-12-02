from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presummap = {0: 1}
        prefixsum = 0
        count = 0
        for i in range(0, len(nums)):
            prefixsum = prefixsum + nums[i]
            # check if there exists any other exists like in the map then again add the sum with the difference of the indices
            # now check the second condition for the remaining sum -k
            if prefixsum - k in presummap:
                count += presummap[prefixsum - k]
            if prefixsum in presummap:
                presummap[prefixsum] += 1
            else:
                presummap[prefixsum] = 1
        return count


# write condition where len==k and return that many instances !

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 1], 2),
        ([1, 2, 3], 3),
        ([1, -1, 0], 0),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7),
        ([], 0),
        ([0, 0, 0], 0),
        ([1, 2, 1, 2, 1], 3),
    ]

    for nums, k in tests:
        try:
            res = sol.subarraySum(nums, k)
        except Exception as e:
            res = f"ERROR: {e}"
        print(f"nums={nums}, k={k} -> {res}")

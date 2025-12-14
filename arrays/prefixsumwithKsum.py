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

        # lets try the two pointer approach
        # left=0
        # right=0
        # sum =nums[0]
        # count=0
        # while(right<len(nums)):
        #     while(left<=right and sum>k):
        #         sum=sum-nums[left]
        #         left=left+1
        #     if(sum==k):
        #         count=count+1
        #     right=right+1
        #     if(right<len(nums)):
        #         sum=sum+nums[right]
        # return count


# the above 2nd method will work only if there are positive numbers in the arry
if __name__ == "__main__":
    sol = Solution()
    tests = [
        # (nums, k, expected)
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 5),
        ([], 0, 0),
        ([0, 0, 0], 0, 6),  # all zero subarrays
        ([1, 2, 1, 2, 1], 3, 4),  # multiple overlapping subarrays
        ([-1, -1, 1], -1, 2),  # negatives
        ([5], 5, 1),  # single element equal k
        ([5], 3, 0),  # single element not equal k
        ([2, -2, 2, -2, 2], 0, 4),  # alternating sums
        ([1000000, -1000000, 0], 0, 3),  # large numbers
    ]

    for nums, k, expected in tests:
        try:
            out = sol.subarraySum(nums, k)
        except Exception as e:
            out = f"ERROR: {e}"
        status = "PASS" if out == expected else "FAIL"
        print(f"nums={nums}, k={k} -> {out} | expected={expected} => {status}")

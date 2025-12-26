from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # better approach failing 2 test cases passed 189/191
        # maxProduct=float("-inf")
        # for i in range(0,len(nums)):
        #     product=1
        #     for j in range(i,len(nums)):
        #         product=product*nums[j]
        #         maxProduct=max(product,maxProduct)
        # return maxProduct
        suffix = 1
        prefix = 1
        n = len(nums)
        maxProduct = float("-inf")
        for i in range(n):
            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]
            maxProduct = max(suffix, maxProduct)
            maxProduct = max(prefix, maxProduct)
        return maxProduct


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([0, 2], 2),
        ([-2, 3, -4], 24),
        ([0, 0, 0], 0),
        ([-1, -2, -9, -6], 108),
        ([-2, -3, 0, -2, -40], 80),
    ]

    for nums, expected in tests:
        try:
            out = sol.maxProduct(list(nums))
        except Exception as e:
            out = f"ERROR: {e}"
        status = "PASS" if out == expected else "FAIL"
        print(
            f"input: {nums[:20]}{'...' if len(nums)>20 else ''} -> output: {out} | expected: {expected} => {status}"
        )

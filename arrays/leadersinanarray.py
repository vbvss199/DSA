class Solution:
    def leaders(self, nums):
        maxEle = float("-inf")
        temp = [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > maxEle and nums[i] > nums[i + 1]:
                maxEle = nums[i]
                if nums[i] not in temp:
                    temp.append(nums[i])
        # temp = temp.sort()
        return temp[::-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], [5]),
        ([1], [1]),
        ([7, 7, 7], [7]),  # duplicates -> only last (strict greater semantics)
        ([1, 2, 2, 1], [2, 1]),  # second 2 and last 1 are leaders
        ([-1, -2, -3], [-1, -2, -3]),  # all decreasing negatives
        ([-3, -2, -1], [-1]),  # increasing negatives -> only last
    ]

    for nums, expected in tests:
        out = sol.leaders(nums)
        ok = out == expected
        status = "PASS" if ok else "FAIL"
        print(f"{nums} -> {out} | expected: {expected} => {status}")

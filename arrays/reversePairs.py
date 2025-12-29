from typing import List


class Solution:
    # the merge logic goes here
    def merge(self, nums, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        while (i <= mid) and (j <= end):
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i = i + 1
            else:
                temp.append(nums[j])
                j = j + 1
        while i <= mid:
            temp.append(nums[i])
            i = i + 1
        while j <= end:
            temp.append(nums[j])
            j = j + 1
        for k in range(len(temp)):
            nums[start + k] = temp[k]

    def countPairs(self, nums, start, mid, end):
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            self.count += j - (mid + 1)

    def mergeSort(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid + 1, end)
            self.countPairs(nums, start, mid, end)
            self.merge(nums, start, mid, end)

    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 3, 2, 3, 1], 2),
        ([2, 4, 3, 5, 1], 3),
        ([5, 4, 3, 2, 1], 4),
        ([], 0),
        ([1], 0),
        ([1, 2, 3, 4], 0),
        ([-5, -5, -5], 3),
        ([2147483647, -2147483648], 1),
    ]

    for arr, expected in tests:
        # Create a copy since the method sorts the list in-place
        arr_copy = list(arr)
        try:
            out = sol.reversePairs(arr_copy)
        except Exception as e:
            out = f"ERROR: {e}"

        status = "PASS" if out == expected else "FAIL"
        print(f"input: {arr} -> output: {out} | expected: {expected} => {status}")

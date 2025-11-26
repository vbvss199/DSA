class Solution:
    # second largest fucntion
    def secondLargest(self, nums, n):
        largest = nums[0]
        sLargest = -1
        for i in range(1, n):
            if nums[i] > largest:
                sLargest = largest
                largest = nums[i]
            elif nums[i] != largest and nums[i] > sLargest:
                sLargest = nums[i]
        return sLargest

    # second smallest function
    def secondSmallest(self, nums, n):
        smallest = nums[0]
        sSmallest = float("inf")
        for i in range(1, n):
            if nums[i] < smallest:
                sSmallest = smallest
                smallest = nums[i]
            elif nums[i] != smallest and nums[i] < sSmallest:
                sSmallest = nums[i]
        return sSmallest

    def secondLargestSmallestElement(self, nums, n):
        sLargest = self.secondLargest(nums, n)
        sSmallest = self.secondSmallest(nums, n)
        return [sLargest, sSmallest]


if __name__ == "__main__":
    sol = Solution()
    nums = [89, 65, 44, 44, 44, 32, 32, 31, 19, 0]
    n = len(nums)
    x = sol.secondLargestSmallestElement(nums, n)
    x
    # [1,2,4,7,7,5]

# solve the largest element in an array in the similar way with O(n) time complexity

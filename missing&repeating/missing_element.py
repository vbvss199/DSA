class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor=nums[0]
        n=len(nums)
        for i in range(1,n):
            xor=xor^nums[i]
        for k in range(1,n+1):
            xor=xor^k
        return xor
#Input: nums = [9,6,4,2,3,5,7,0,1]
#Output: 8
#can also be solved by using the sum of the elements in the array and the sum of the indices and subtract to get the missing element !
#but xor is the faster as it involves bits and the time complexity is O(n) and space complexity is O(1)
#driver code
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
#Output: 8
# Time complexity: O(n)
# Space complexity: O(1)

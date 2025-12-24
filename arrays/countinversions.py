# class Solution:
#     def merge(self, nums, start, mid, end):
#         i=start
#         j=mid+1
#         while((i<=mid) and (j<=end)):
#             if(nums[i]<=nums[j]):
#                 self.temp.append(nums[i])
#                 i=i+1
#             # this is the place where we say right is smaller
#             else:
#                 self.temp.append(nums[j])
#                 self.count+=(mid-i+1)
#                 j=j+1
#         while(i<=mid):
#             self.temp.append(nums[i])
#             i=i+1
#         while(j<=end):
#             self.temp.append(nums[j])
#             j=j+1
#         for k in range(len(self.temp)):
#             nums[start+k]=self.temp[k]

#     def mergesort(self,nums,start,end):
#         if (start < end):
#             mid=(start+end)//2
#             self.mergesort(nums,start,mid)
#             self.mergesort(nums,mid+1,end)
#             self.merge(nums, start, mid, end)
#     def sortArray(self, nums: list[int]) -> list[int]:
#         start=0
#         end=len(nums)-1
#         self.temp = [0] * len(nums)
#         # step1 dividing arrays into two parts and sending them to merge formuale
#         self.mergesort(nums,start,end)
#         return nums


class Solution:
    def merge(self, nums, start, mid, end):
        temp = []
        i = start
        j = mid + 1
        while (i <= mid) and (j <= end):
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i = i + 1
            else:
                temp.append(nums[j])
                self.count += mid - i + 1
                j = j + 1
        while i <= mid:
            temp.append(nums[i])
            i = i + 1
        while j <= end:
            temp.append(nums[j])
            j = j + 1
        for k in range(len(temp)):
            nums[start + k] = temp[k]

    def mergesort(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            self.mergesort(nums, start, mid)
            self.mergesort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def inversionCount(self, arr):
        # Code Here
        self.count = 0
        self.mergesort(arr, 0, len(arr) - 1)
        return self.count

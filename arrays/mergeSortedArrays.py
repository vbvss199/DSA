class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # left = m - 1
        # right = n - 1
        # k = m + n - 1
        # # ned to merge two arrays such
        # while right >= 0:
        #     if left >= 0 and nums1[left] > nums2[right]:
        #         nums1[k] = nums1[left]
        #         left = left - 1
        #     else:
        #         nums1[k] = nums2[right]
        #         right = right - 1
        #     k = k - 1
        # return nums1
        # takeforward approach
        left = m - 1
        right = 0
        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left = left - 1
                right = right + 1
            else:
                break
        return nums1[:m] + nums2


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1, 2, 3], 3, [], 0),
        ([0, 0, 0], 0, [2, 5, 6], 3),
        ([1, 1, 1, 0, 0, 0], 3, [1, 1, 2], 3),
        ([1, 2, 4, 0, 0, 0], 3, [5, 5, 6], 3),
    ]
    for nums1, m, nums2, n in tests:
        print(f"Before: nums1={nums1}, nums2={nums2}, m={m}, n={n}")
        print(sol.merge(nums1, m, nums2, n))
        print(f"After:  nums1={nums1}, nums2={nums2}")
        print("-" * 40)

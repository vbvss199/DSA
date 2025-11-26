class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        intersection = []
        while (i < n1) and (j < n2):
            # as 2is <3 so move forward there will be no partner left so we need to have a higher number i.e why we move the variable i
            if nums1[i] < nums2[j]:
                i = i + 1
            elif nums2[j] < nums1[i]:
                j = j + 1
            elif nums1[i] == nums2[j]:
                intersection.append(nums2[j])
                i = i + 1
                j = j + 1
        return intersection


if __name__ == "__main__":
    sol = Solution()

    # Note: algorithm expects input arrays to be sorted.
    tests = [
        ([1, 2, 2, 1], [2, 2]),
        ([1, 1, 2, 2, 3], [1, 2, 2, 4]),
        ([1, 2, 3], [4, 5, 6]),  # no intersection
        ([4, 9, 5], [9, 4, 9, 8, 4]),  # empty left
        ([1, 2, 3], []),  # empty right
    ]

    for a, b in tests:
        print(f"{a} ∩ {b} -> {sol.intersection(a,b)}")

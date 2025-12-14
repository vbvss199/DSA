from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = float("-inf")
        temp = [-1]
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > maxElement and arr[i - 1] > arr[i]:
                maxElement = arr[i]
                temp.append(maxElement)
            else:
                maxElement = max(maxElement, arr[i])
                temp.append(maxElement)
        return temp[::-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, -1]),
        ([1, 2, 3, 4, 5], [5, 5, 5, 5, -1]),
        ([2, 2, 2], [2, 2, -1]),
        ([], []),
        ([9, -1, -2, 7], [7, 7, 7, -1]),
        ([1, -1], [-1, -1]),
        ([-5], [-1]),
        ([0, 0, 1, 0], [1, 1, 0, -1]),
    ]

    for arr, expected in tests:
        try:
            out = sol.replaceElements(list(arr))
        except Exception as e:
            out = f"ERROR: {e}"
        status = "PASS" if out == expected else "FAIL"
        print(f"input: {arr} -> output: {out} | expected: {expected} => {status}")

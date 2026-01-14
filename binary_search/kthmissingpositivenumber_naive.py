from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # lets go directly with binary search approach
        # k is the target
        # brute force
        for i in range(len(arr)):
            if arr[i] <= k:
                k = k + 1
            else:
                break
        return k


if __name__ == "__main__":
    # Sample tests
    sol = Solution()
    tests = [
        ([2, 3, 4, 7, 11], 5),  # expected 9
        ([1, 2, 3, 4], 2),  # expected 6
        ([], 1),  # expected 1
    ]
    for arr, k in tests:
        print(f"arr={arr}, k={k} -> {sol.findKthPositive(arr, k)}")

    # Optional: simple stdin parsing (space-separated array on first line, k on second)
    try:
        import sys

        data = sys.stdin.read().strip().split()
        if data:
            # first N numbers are array, last token is k
            *arr_tokens, k_token = data
            arr = list(map(int, arr_tokens)) if arr_tokens else []
            k = int(k_token)
            print(sol.findKthPositive(arr, k))
    except Exception:
        pass

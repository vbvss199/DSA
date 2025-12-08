from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minEle = float("inf")
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minEle:
                minEle = prices[i]
            profit = max(profit, prices[i] - minEle)

        return profit


if __name__ == "__main__":
    sol = Solution()
    tests = [
        [7, 1, 5, 3, 6, 4],  # buy at 1, sell at 6 -> 5
        [7, 6, 4, 3, 1],  # decreasing -> 0
        [1, 2, 3, 4, 5],  # increasing -> 4
        [2, 1, 2, 0, 1],  # best 1
        [3, 3, 5, 0, 0, 3, 1, 4],  # best 6 (buy 0 sell 4)
        [1, 2],  # small increasing -> 1
        [2, 1],  # small decreasing -> 0
    ]

    for prices in tests:
        try:
            res = sol.maxProfit(prices)
        except Exception as e:
            res = f"ERROR: {e}"
        print(f"prices={prices} -> maxProfit={res}")

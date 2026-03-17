# User function Template for python3


class Solution:
    def generateSubSequences(self, arr, i, sum, K):
        # the base case is when we reach the array end
        if sum > K:
            return False
        if i == self.n:
            return sum == K

        if self.generateSubSequences(arr, i + 1, sum + arr[i], K):
            return True

        # not pick function call
        if self.generateSubSequences(arr, i + 1, sum, K):
            return True
        return False

    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        # and a empty data strcture (array) ds to store the elements and a running sum which is 0
        self.n = len(arr)
        return self.generateSubSequences(arr, 0, 0, K)

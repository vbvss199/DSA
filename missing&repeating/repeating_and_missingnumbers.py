class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        xor_1=A[0]
        for i in range(1,n):
            xor_1=xor_1^A[i]
        for j in range(1,n+1):
            xor_1=xor_1^j
        #finding the right set bit 
        right_set_bit = xor_1 & ~(xor_1 - 1)
        
        x,y=0,0
        for i in range(0,n):
            if right_set_bit & A[i]:
                x=x^A[i]
            else:
                y=y^A[i]
        for j in range(1,n+1):
            if right_set_bit & j:
                x=x^j
            else:
                y=y^j
        if x in A:
            return [x,y]
        else:
            return [y,x]

#driver code 
print(Solution().repeatedNumber([3, 1, 3, 4, 2]))

# the other way of logic is to create a map DS and assign keys with the numbers and the values with their count 
# iterate over keys and values to find the missing and repeated elements where the space complexity using this approach is O(n)
#O(1) space and O(n) time ? 
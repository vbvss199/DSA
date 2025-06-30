def LinearSearch(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
        
#driver code
arr=[1,2,3,4,5,6,7,8]
n=len(arr)
target=5
print(LinearSearch(arr,n,target))
# Time complexity: O(n)
# Space complexity: O(1)
# This code implements a linear search algorithm in Python.
#if we use the simple if else block it will return the -1 after very first mismatch so keep -1 if nothing matches at the end of the loop.
#Yes—the return -1 is indented inside the for, so you’ll bail out on the very first element that doesn’t match. You want to scan all n elements before giving up. Move the “not found” return outside the loop:
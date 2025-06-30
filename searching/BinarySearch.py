def BinarySearch(arr,n,target):
    start=0
    end=n-1
    while(start<=end):
        mid=start+ (end-start)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return -1
#driver code
arr=[1,2,3,4,5,6,7,8]
n=len(arr)
target=6
print(BinarySearch(arr,n,target))
#the array must be sorted in ascending order for binary search to work.
# Time complexity: O(log n).
# Space complexity: O(1).
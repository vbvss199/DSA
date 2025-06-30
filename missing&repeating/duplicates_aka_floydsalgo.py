def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        print(slow,fast)
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3


#another version of the above is hare tortoise algorithm can be seen in the Code References.txt
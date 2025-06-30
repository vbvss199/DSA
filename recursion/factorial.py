def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
#driver code
print(factorial(5))
#implementation of factorial using recursion
#the internal call stack is used to store the state of each recursive call
#the function calls itself with a smaller value of n until it reaches the base case
#the time complexity is O(n) and the space complexity is O(n) due to the call stack ,time complexity is calcuated by substituion method!
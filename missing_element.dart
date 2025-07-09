class Solution {
  int missingNumber(List<int> nums) {
    // int n = nums.length;
    // int k = 0;
    // for (int i = 1; i < n + 1; i++) {
    //   if (!nums.contains(i)) {
    //     k = i;
    //   }
    // }
    // return k;

    // the alternate approach is to find using the totoal sum minus the expected sum
    int n = nums.length;
    int expected_sum = n * (n + 1) ~/ 2;
    // Step 1: 1 + 2 = 3,Step 2: 3 + 3 = 6,Step 3: 6 + 4 = 10
    // where a is previous element and b is current
    int actual_sum = nums.reduce((a, b) => a + b);
    return expected_sum - actual_sum;
  }
}

void main() {
  final solution = Solution();

  List<int> nums = [9, 6, 4, 2, 3, 5, 7, 0, 1];
  int result = solution.missingNumber(nums);
  print("Missing number: $result"); // Expected: 2
}

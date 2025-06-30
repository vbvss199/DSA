class Solution {
  int removeElement(List<int> nums, int val) {
    nums.removeWhere((ele) => (ele==val));
    return nums.length;
  }
}
//     if(nums.contains(val)){
//       nums.remove(val);
//     }
//   return nums.length;
//   }


//func
// Function bar = (int param ) => return 1;
// int foo() {return 1;}
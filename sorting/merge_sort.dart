//merge sort works on the divide and conquer
//repeatdely divide the array into two parts
//find mid element and divide array into two parts namely left array and right array
//now the left array and right array splitted into two equal halves and if the length is odd divide it on any side
//recursively repeat it again and again  until we are left with a single element
// left with a single element is a base condition and from there we going to back track

// the above part is dividing into equal halves by finding the mid element now the second part

// 2nd part
// merge the parts to create a sorted array when we backtrack from bottom
//the problem is how to sort the left and right arrays using back tracking.

// start with finding the mid using the start and end indices with the optimized one for finding the mid element

class Solution {
  List<int> sortArray(List<int> nums,int start,int end) {
    // using merge sort
    mergeSort(nums, start, end);
    return nums;
  }
}

// 2nd step
void merge(List<int> arr, int start, int end, int mid) {
  List<int> temp = [];
  int i = start;
  int j = mid + 1;
  while (i <= mid && j <=end) {
    if (arr[i] <= arr[j]) {
      temp.add(arr[i]);
      i++;
    } else {
      temp.add(arr[j]);
      j++;
    }
  }
  // copy remainig elements if some are left !
  while (i <= mid) {
    temp.add(arr[i]);
    i++;
  }
  while (j <= end) {
    temp.add(arr[j]);
  j++;
  }
  for (int idx = 0; idx < temp.length; idx++) {
    arr[start + idx] = temp[idx];
  }
}

// 1st step
void mergeSort(List<int> arr, int start, int end) {
  if (start < end) {
    int mid = start + (end - start) ~/ 2;
    mergeSort(arr, start, mid);
    mergeSort(arr, mid + 1, end);
    merge(arr, start, end, mid);
  }
}

void main() {
  final solution = Solution();

  // Example input list
  List<int> nums = [5, 2, 3, 1];

  // Call the sortArray method
  List<int> sorted = solution.sortArray(nums,0,nums.length-1);

  // Print the result
  print('Sorted array: $sorted');
}

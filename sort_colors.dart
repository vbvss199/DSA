class Solution {
  List<int> sortColors(List<int> nums,int start,int end) {
    mergeSort(nums, start, end);
  return nums;
  }
}

void merge(List<int> nums,int start,int end ,int mid){
  int i=start;
  int j =mid+1;
  List<int> temp=[];
  while(i<=mid && j<=end){
    if(nums[i]<=nums[j]){
      temp.add(nums[i]);
      i=i+1;
    }
    else{
      temp.add(nums[j]);
      j++;
    }
  }
  while(i<=mid){
    temp.add(nums[i]);
    i=i+1;
    }
  while(j<=end){
      temp.add(nums[j]);
      j=j+1;
    }
  for (int idx=0;idx<temp.length;idx++){
      nums[start+idx]=temp[idx];
    }
  }

  void mergeSort(List<int> nums,int start,int end){
    if(start<end){
      int mid=start+(end-start)~/2;
      mergeSort(nums,start,mid);
      mergeSort(nums,mid+1,end);
      merge(nums,start,end,mid);
    }
  }

void main() {
  final solution = Solution();

  // Example input list
  List<int> nums = [2,0,2,1,1,0];;

  // Call the sortArray method
  List<int> sorted = solution.sortColors(nums,0,nums.length-1);

  // Print the result
  print('Sorted array: $sorted');
}

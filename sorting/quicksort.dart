void main() {
  List<int> arr = [10, 7, 8, 9, 1, 5];
  int n = arr.length;

  quickSort(arr, 0, n - 1); // Call to your quick sort implementation

  print("Sorted array is: $arr");
}

void quickSort(List<int> arr, int low, int high) {
  if (low < high) {
    int pivotIndex = partition(arr, low, high);
    quickSort(arr, low, pivotIndex);
    quickSort(arr, pivotIndex + 1, high);
  }
}

int partition(List<int> arr, int low, int high) {
  int pivot = arr[low];
  int i = low;
  for (int j = i + 1; j <= high; j++) {
    if (arr[j] < pivot) {
      i = i + 1;
      swap(arr, i, j);
    }
  }
  swap(arr, low, i);
  return i; //pivot index
}

void swap(List<int> arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

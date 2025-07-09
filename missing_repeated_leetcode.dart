class Solution {
  List<int> findMissingAndRepeatedValues(List<List<int>> grid) {
    int n = grid.length * grid[0].length;
    List<int> flattendList = grid.expand((x) => x).toList();
    int actualSum = flattendList.reduce((a, b) => a + b);
    int expectedSum = n * (n + 1) ~/ 2;
    int squaresActualSum = flattendList.fold(0, (a, b) => a + b * b);
    int squaresExpectedSum = n * (n + 1) * (2 * n + 1) ~/ 6;
    int x = actualSum - expectedSum; // a-b
    int y =
        (squaresActualSum - squaresExpectedSum) ~/
        x; // a+b which we get from a+b*a-b//a-b
    int x1 = (x + y) ~/ 2; //duplicate
    int x2 = x1 - x; //repeating element
    return [x1, x2];
  }
}

void main() {
  final solution = Solution();
  List<List<int>> grid = [
    [9, 1, 7],
    [8, 9, 2],
    [3, 4, 6],
  ];
  List<int> result = solution.findMissingAndRepeatedValues(grid);
  print("missing and duplicate numbers are $result");
}
// fold reduce map expand 
// map- operation on each iterable element,Transforms each element of a collection and returns a new Iterable
// Transforms each element to multiple values (or a collection) and flattens the result.
// reduce Combines all elements into a single value by applying a function repeatedly. just like sum applies on a and b where a is first element and b is 2nd element  
// fold :ike reduce(), but lets you provide an initial value — making it safer and more flexible.
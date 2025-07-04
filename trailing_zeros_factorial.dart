class Solution {
  int trailingZeroes(int n) {
    //implement logic here
    int count=0;
    while(n%10==0){
      count=count+1;
      n= n~/10;
    }
    return count;
  }
}

int fact(int n){
  if( n==0 || n==1){
    return 1;
  }
  else{
    return n*fact(n-1);
  }
}
void main() {
  final solution = Solution();

  // Define a fixed number instead of reading from stdin
  final int n = 10;  // you can change this to any value you like
  final result = solution.trailingZeroes(fact(n));
  print('Number of trailing zeros in ${n}! is $result');
}

// this method failed coz of the factorial calculation first and then counting by stripping so better with calcualting the factorial try to find the trailing zeros

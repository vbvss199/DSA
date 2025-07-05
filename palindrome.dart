class Solution {
  bool isPalindrome(int x) {
    int original=x;
    String reverse="";
    if(x<0){
      return false;
    }
    while(x>0){
      int k=x%10;
      reverse=reverse+k.toString();
      x=x~/10;
    }
    if(reverse==original.toString()){
      return true;
    }
    else{
      return false;
    }
  }
}
void main() {
  final solution = Solution();

  int number = 121; // you can change this to test other inputs
  bool result = solution.isPalindrome(number);

  print("Is $number a palindrome? $result");
}

void main(){
  String s="MCMXCIV";
  romanToInt(s);
}

void romanToInt(String s) {
  //var I =1,V=5,X=10,L=50,C=100,D=500,M=1000;
  int sum=0;
  int difference=0;
  var romans={
    'I':1,
    'V':5,
    'X':10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
  };
  List<String> nums=s.split("");
  List<int> nums_int=[];
  nums.forEach((String ele){
    nums_int.add(romans[ele]!);
  });
  //print(nums_int);
  // order does matter
    if (nums_int[0]<nums_int[1] ){
      nums_int.forEach((ele){
        difference=ele-difference;
      });
    }
  //order doesn't matter 
    else{
      nums_int.forEach((ele){
        sum=sum+ele;
      });
    }
  print(difference);
  print(sum);
  }

void main(){
  String s="MCMXCIV";
  romanToInt(s);
}

void romanToInt(String s) {
  //var I =1,V=5,X=10,L=50,C=100,D=500,M=1000;
  int sum=0;
  var romans={
    'I':1,
    'V':5,
    'X':10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
  };

int checkOrder(List<String> t){
  if (romans[t[0]]! >= romans[t[1]]!){
    return romans[t[0]]!+romans[t[1]]!;
  }
  else{
     return romans[t[1]]!-romans[t[0]]!;
  }
}

List<int> nums_int_mod=[];
// special function 
List<int> specialFunction(List<String> l){
  l.forEach((String element){
    List<String> test = element.split("");
    nums_int_mod.add(checkOrder(test));
  });
  return nums_int_mod;
  }

  // splitting to first character and two charcters each 
  String firstCharcter=s[0];
  String remainingCharcter=s.substring(1);
  List<String> nums_mod=[firstCharcter];
  for(int i=0;i<remainingCharcter.length;i+=2){
    int endIndex=i+2;
    nums_mod.add(remainingCharcter.substring(i,endIndex));
  }
  // now check the list numbers sum separately from 2nd number whether order matters or not  if order matters calculate the difference else calculate the sum and return the array with the respective elements
  // just like nums_mod=["M","CM","XC","IV"] should return [1000,900,90,4] lastly add this thing
  nums_int_mod.add(romans[nums_mod[0]]!);
  List<int> finalList=specialFunction(nums_mod.sublist(1));
  print(finalList);
  finalList.forEach((ele){
    sum+=ele;
  });
  print(sum);
  }

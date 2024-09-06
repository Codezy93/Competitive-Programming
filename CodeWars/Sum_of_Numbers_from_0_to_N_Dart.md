
# Sum of Numbers from 0 to N Dart

Date: 06-09-2024

## Solution
#### Python
```python
class SequenceSum{
  static String showSequence(int n)
  {
    String s = "";
    int sum = 0;
    for(int i=0; i <= n; i++){
      sum = sum + i;
      if(i==n){
        s = s + "$i";
      }
      else{
        s = s + "$i+";
      }
    }
    if(s.length == 1){
      s = s + "=$sum";
    }
    else if(n<0) {
      s = "$n<0";
    }
    else{
      s = s + " = $sum";
    }
    return s;
  }
}
```
        
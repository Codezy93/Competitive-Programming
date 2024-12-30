
# Ones and Zeros

Date: 07-09-2024

## Solution
#### Python
```python
import 'dart:math';
int binaryArrayToNumber(List<int> arr) {
  int num = 0;
  for (int i = 0; i < arr.length; i++) {
    num += arr[i] * pow(2, (arr.length - 1 - i)).toInt();
  }
  return num;
}
```
        

# Reverse String

Date: 28-09-2024

## Solution
#### Python
```python
#include <string>
using namespace std ; 
string reverseString (string str )
{
  string rev = "";
  for(int i = 0; i<str.length(); i++){
    rev = str[i] + rev;
  }
  return rev;
}
```
        

# Vector-Sort

Date: 22-08-2024

## Solution
#### Python
```python
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int length;
    vector<int> arr;
    cin >> length;
    for(int i = 0; i < length; i++){
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    sort(arr.begin(),arr.end());
    for(int i = 0; i < length; i++){
        string temp = std::to_string(arr[i]);
        cout << temp << " ";
    }
    return 0;
}
```
        
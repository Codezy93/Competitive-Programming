
# Vector Erase

Date: 26-08-2024

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
    int length, temp, m, n, o;
    cin >> length;
    vector<int> arr(length);
    for(int i = 0; i<length; i++){
        cin >> temp;
        arr[i] = temp;
    }
    cin >> o;
    arr.erase(arr.begin() + o - 1);
    cin >> m >> n;
    arr.erase(arr.begin() + m - 1, arr.begin() + n - 1);
    cout << arr.size() << endl;
    for(int i = 0; i<arr.size(); i++){
        cout << arr[i] << " ";
    }
    return 0;
}
```
        
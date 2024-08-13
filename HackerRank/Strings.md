
# Strings

Date: 13-08-2024

## Solution
#### Python
```python
#include <iostream>
#include <string>
using namespace std;
int main() {
	string a,b,c;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a+b << endl;
    c = a[0];
    a[0] = b[0];
    b[0] = c[0];
    cout << a + " " + b << endl;
    return 0;
}
```
        
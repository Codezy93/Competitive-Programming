
# Sets-STL

Date: 29-08-2024

## Solution
#### Python
```python
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
int main() {
    set<int> s;
    int iteration, query, input;
    cin >> iteration;
    for(int i = 0; i < iteration; i++){
        cin >> query >> input;
        if(query == 1){
            s.insert(input);
        }
        else if(query == 2){
            s.erase(input);
        }
        else{
            set<int>::iterator itr = s.find(input);
            if(itr != s.end()){
                cout << "Yes" << endl;
            }
            else{
                cout << "No" << endl;
            }
        }
    }   
    return 0;
}
```
        
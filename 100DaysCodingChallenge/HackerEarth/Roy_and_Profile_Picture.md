
# Roy and Profile Picture

Date: 10-08-2024

## Solution
#### Python
```python
l = int(input())
for _ in range(0, int(input())):
    w, h = map(int, input().split())
    if (w<l) or (h<l):
        print("UPLOAD ANOTHER")
    else:
        if(w==h):
            print("ACCEPTED")            
        else:
            print("CROP IT")
```
        
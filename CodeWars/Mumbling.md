
# Mumbling

Date: 28-08-2024

## Solution
#### Python
```python
def accum(st):      
    return "-".join([j.upper() + (j*i) for i, j in enumerate(st.lower())])
```
        
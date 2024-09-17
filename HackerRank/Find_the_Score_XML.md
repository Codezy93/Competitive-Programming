
# Find the Score XML

Date: 17-09-2024

## Solution
#### Python
```python
def get_attr_number(node):
    return len(node.items()) + sum([get_attr_number(x) for x in node])
```
        
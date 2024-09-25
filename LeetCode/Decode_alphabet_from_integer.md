
# Decode alphabet from integer

Date: 25-09-2024

## Solution
#### Python
```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        map = {'26#': 'z', '25#': 'y', '24#': 'x', '23#': 'w', '22#':
        'v', '21#': 'u', '20#': 't', '19#': 's', '18#': 'r', '17#': 'q',
        '16#': 'p', '15#': 'o', '14#': 'n', '13#': 'm', '12#': 'l', '11#':
        'k', '10#': 'j', '9': 'i', '8': 'h', '7': 'g', '6': 'f', '5': 'e',
        '4': 'd', '3': 'c', '2': 'b', '1': 'a'}
        for i in map:
            s = s.replace(i, map[i])
        return s
```
        
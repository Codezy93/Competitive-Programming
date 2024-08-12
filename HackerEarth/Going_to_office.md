
# Going to office

Date: 12-08-2024

## Solution
#### Python
```python
distance = int(input())
oc, of, od = [int(x) for x in input().split()]
cs, cb, cm, cd = [int(x) for x in input().split()]
online_fare = oc + ((distance-of) * od)
classic_fare = cb + ((distance/cs)*cm) + (distance*cd)
if online_fare > classic_fare:
    print('Classic Taxi')
else:
    print('Online Taxi')
```
        
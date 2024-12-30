# Number of people in bus

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
def number(bus_stops):
    return sum([x[0]-x[1] for x in bus_stops])
 ```
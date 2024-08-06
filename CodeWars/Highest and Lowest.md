# Highest and Lowest

Platform: CodeWars

Date: 05/08/2024

## Problem
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

## Input
String of n integers seperated by space.

## Output
String of highest and lowest number seperated by space.

## Solution
```python
def high_and_low(numbers):
    numbers = numbers.split(" ")
    list_num = [int(x) for x in numbers]
    return f"{max(list_num)} {min(list_num)}"
```
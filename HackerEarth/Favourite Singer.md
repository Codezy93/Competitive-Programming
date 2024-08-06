# Favourite Singer

Platform: HackerEarth

Date: 06/08/2024

## Problem
Bob has a playlist of songs, each song has a singer associated with it (denoted by an integer)
Favourite singer of Bob is the one whose songs are the most on the playlist
Count the number of Favourite Singers of Bob

## Input 
The first line contains an integer, denoting the number of songs in Bob's playlist.
The following input contains integers, integer denoting the singer of the song.

## Output
Output a single integer, the number of favourite singers of Bob

Note: Use 64 bit data type

## Solution

```python
from collections import Counter

# Read input
length = int(input())
play = input().split()

# Count occurrences of each item
play_count = Counter(play)

# Find the maximum count
max_count = max(play_count.values())

# Count how many items have the maximum count
most_common_count = sum(1 for count in play_count.values() if count == max_count)

# Output the result
print(most_common_count)
```
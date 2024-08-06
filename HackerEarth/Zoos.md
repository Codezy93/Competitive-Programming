# Zoos

Platform: HackerEarth

Date: 06/08/2024

## Problem
You are required to enter a word that consists of x and y.
 that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2*x = y
Determine if the entered word is similar to word zoo.
For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

## Input
First line: A word that starts with several Zs and continues by several Os.

## Output
Yes or No based on the string.

## Soultion
```python
inp = input()
if inp.count('z')*2 == inp.count('o'):
    print('Yes')
else:
    print('No')
```
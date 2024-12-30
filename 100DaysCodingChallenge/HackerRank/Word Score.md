# Word Score

Date: 05/08/2024

## Solution
#### Python
```python

def vowels(word):
    length = len(word)
    vowel = "aeiouyAEIOUY"
    for v in vowel:
        word = word.replace(v, "")
    if (length - len(word))%2 == 0:
        return 2
    else:
        return 1

def score_words(words):
    score = 0
    for word in words:
        score += vowels(word)
    return score

n = int(input())
words = input().split()
print(score_words(words))
```
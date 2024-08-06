# Word Score

Platform: HackerRank

Date: 05/08/2024

## Problem
Consider that vowels in the alphabet are ``` a, e, i, o, u and y.```

Function ```score_words``` takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is  if the word contains an even number of vowels. Otherwise, the score of this word is . The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function score_words such that it returns a correct score.

Your function will be tested on several cases by the locked template code.

## Input
The input is read by the provided locked code template. In the first line, there is a single integer  denoting the number of words. In the second line, there are  space-separated lowercase words.

## Constraints
Each word has at most  letters and all letters are English lowercase letters

## Output
The output is produced by the provided and locked code template. It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.

## Solution
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
# Passing the Parcel

Date: 2024-11-06 00:00:00

## Solution

#### Python
```python
n  = int(input())
st = [True]*n
song = input()
ne = len(song)
c = 0
j=0
i=0
while c<n-1:
    if i>=ne:
        i = i%ne
    if j>=n:
        j = j%n
    if song[i] =='a':
        if st[j] != False:
            i+=1
            j+=1
        else:
            j+=1
    elif song[i] == 'b':
        if st[j] != False:
            c+=1
            i+=1
            st[j] = False
            j+=1
        else:
            j+=1
for i in range(len(st)):
    if st[i] == True:
        print(i+1)
        break
 ```
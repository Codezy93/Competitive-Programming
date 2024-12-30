
# Ali and Helping innocent people

Date: 09-08-2024

## Solution
#### Python
```python
code = input()
digits = [str(x) for x in range(0, 10)]
letter = ['A', 'E', 'I', 'O', 'U', 'Y']
if (code[2] not in letter):
    if((int(code[0]) + int(code[1]))%2 == 0):
        if((int(code[3]) + int(code[4]))%2 == 0):
            if((int(code[4]) + int(code[5]))%2 == 0):
                if((int(code[7]) + int(code[8]))%2 == 0):
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')
        else:
            print('invalid')
    else:
        print('invalid')
else:
    print('invalid')
```
        
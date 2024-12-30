
# Sum of Numbers

Date: 20-08-2024

## Solution
#### Python
```python
int get_sum(int a, int b)
{
  int sum, n, m;
  if(a>b){
    n = b;
    m = a;
  }
  else if(a<b){
    n = a;
    m = b;
  }
  else{
    return a;
  }
  sum = 0;
  for(int i = n; i<=m; i++){
    sum += i;
  }
  return sum;
}
```
        
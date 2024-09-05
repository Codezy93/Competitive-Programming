
# Youre a Square

Date: 05-09-2024

## Solution
#### Python
```python
isSquare(n) {
  if(n<0){
    return false;
  }
  else{
    int count = 0;
    while(true){
      if(count*count < n){
        count += 1;
      }
      else if(count*count==n){
        return true;
      }
      else{
        return false;
      }
    }
  }
}
```
        
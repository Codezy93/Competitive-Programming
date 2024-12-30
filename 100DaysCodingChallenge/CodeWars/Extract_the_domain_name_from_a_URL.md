# Extract the domain name from a URL

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
def domain_name(url):
    replace = ["https://", "http://", "www."]
    for i in replace:
        url = url.replace(i, "")
    return url.split(".")[0]
 ```
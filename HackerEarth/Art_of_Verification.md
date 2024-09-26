
# Art of Verification

Date: 26-09-2024

## Solution
#### Python
```python
url = input()
url = url.replace("http://www.cleartrip.com/signin/service?username=", "")
url = url.split("&pwd=")
username = url[0]
url = url[1]
url = url.split("&profile=")
pwd = url[0]
url = url[1]
url = url.split("&role=")
profile = url[0]
url = url[1]
url = url.split("&key=")
role = url[0]
key = url[1]
print(f"username: {username}")
print(f"pwd: {pwd}")
print(f"profile: {profile}")
print(f"role: {role}")
print(f"key: {key}")
```
        
# import requests

# url = "http://192.168.10.110:81/api/users"

# payload={}
# headers = {
#     "Authorization": "Bearer iqrlA0Om2dzarsh5vj4KnteDEYCyc8gWsnEhfTG3pD6Ljstg",
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }

# response = requests.get(url, headers=headers, data=payload)

# print(response.json())

url = "http://192.168.10.110:81/api/users"

if not url.endswith("/"):
    url = url + "/"

print(url)
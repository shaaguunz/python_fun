import requests
r = requests.get("https://www.udemy.com")
print("status :",r.status_code)
print(r.text)

f = open("page.html","w+")
f.write(r.text)

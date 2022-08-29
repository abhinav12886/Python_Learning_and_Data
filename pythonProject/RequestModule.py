import requests

#
# r = requests.get("https://www.google.com/search?q=request+module+in+python&sxsrf=ALeKk01SHaI80o-IQN7VGM6VIsbaX5fc2Q%3A1627374700257&ei=bMT_YJ6RD9i65OUPn8CJYA&oq=request+module+in+python&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgIIADIICAAQFhAKEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoECAAQQ0oECEEYAFCMFFieKmCcLGgBcAJ4AIABywSIAdATkgEJMC43LjMuNS0xmAEAoAEBqgEHZ3dzLXdpesgBCcABAQ&sclient=gws-wiz&ved=0ahUKEwie97KX64LyAhVYHbkGHR9gAgwQ4dUDCA8&uact=5")
# print(r.text)
# print(r.status_code)

url = "https://www.w3schools.com/python/default.asp"
data = {
    "p1": 4,
    "p2": 3
}
r = requests.post(url, data)
print(r.text)
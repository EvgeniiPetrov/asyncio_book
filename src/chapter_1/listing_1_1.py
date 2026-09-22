import requests

request = requests.get("https://mail.ru")
items = request.headers.items()
print(items)
headers = [f"{key} : {header}" for key, header in items]
print("****")
print(headers)
formatted_haeders = "\n".join(headers)
print("****")
print(formatted_haeders)
with open("headers.txt", "w") as file:
    file.write(formatted_haeders)

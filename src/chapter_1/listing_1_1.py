from urllib.parse import urlparse

import requests

site_name = "https://ya.ru"
out_file_name = urlparse(site_name).netloc + ".txt"
request = requests.get(site_name)
items = request.headers.items()
headers = [f"{key} : {header}" for key, header in items]
headers.sort(key=lambda s: s.split(" : ", 1)[0].lower())
formatted_headers = "\n".join(headers)

with open(out_file_name, "w") as file:
    file.write(formatted_headers)

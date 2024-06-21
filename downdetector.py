import requests
import re

url = "https://gist.github.com/PauloOliveiraNOC/58db8fa472f43397bdbb73421025cf92.js"


response = requests.get(url)
content = response.text


pattern = r'(http://downdetector\.com\.br/fora-do-ar/[\w-]+)/Status:(\d+)'
matches = re.findall(pattern, content)


data_dict = {url: int(status) for url, status in matches}


with open('resultados.txt', 'w') as file:
    for url, status in data_dict.items():
        file.write(f"{url}/Status:{status}\n")

print("Results have been saved to 'resultados.txt'")

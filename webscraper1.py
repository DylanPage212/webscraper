from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3080-ti-rtx-3080-ti-gaming-x-trio-12g/p/N82E16814137650?Description=gpu&cm_re=gpu-_-14-137-650-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent

strong = parent.find("strong")

print(strong.string)



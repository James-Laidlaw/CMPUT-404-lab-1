import requests


sourcecode = requests.get("https://raw.githubusercontent.com/James-Laidlaw/CMPUT-404-lab-1/main/getGoogle.py")

print(sourcecode.content)
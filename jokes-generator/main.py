import requests

joke = requests.get("https://official-joke-api.appspot.com/jokes/programming/random").json()[0]

print(joke["setup"])
print(joke["punchline"])


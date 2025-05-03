import pandas as pd
import json

# data = pd.read_json("https://api.sampleapis.com/beers/ale")
# print(data.head())


# from file
with open('beer.json') as fp:
    data = json.load(fp)

jData = pd.DataFrame(data)
print(jData)
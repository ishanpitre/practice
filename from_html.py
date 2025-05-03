import pandas as pd
data = pd.read_html("https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Countries")
print(data[12])

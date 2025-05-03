import pandas as pd

dict1 ={
    "id":[1,2,3,4,5,7],
    "name":["ishan","sahil","ram","shyam","om","kunal"],
    "salary":[10900000,3243342342,5445,533,35543,534]
}
df = pd.DataFrame(dict1,index=['a','b','c','d','e','f'])

# print(df.head())
# print(df.tail())

# print(df.sample(2))  # give sample data randomly 

# print(df.select_dtypes('O'))  #filter will give only objects
# print(df.select_dtypes('int'))
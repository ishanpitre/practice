#version of pandas 2.2
import pandas as pd

dict1 ={
    "id":[1,2,3,4,5,7],
    "name":["ishan","sahil","ram","shyam","om","kunal"],
    "salary":[10900000,3243342342,5445,533,35543,534]
}
df = pd.DataFrame(dict1,index=['a','b','c','d','e','f'])
# print(df)

# print(df.shape)

# print(df.columns)

print(df.get('name'),0) # will give data of name and if given parameter is not present then will return 0 will not give error

# print(df[['id','salary']])

# a= df[[col for col in df.columns if col not in['salary']]]
# print(a)

# b= df[[col for col in df if col in ['name']]]
# print(b)

# print(df.index)

# print(df.dtypes)  #in pandas string are called object

# print(df.size)   #total number of elements is size

# print(df.ndim)  # 2d cause rows and cols

# print(df.memory_usage())

# print(df.describe(include='O'))  #calculate integers to calculate objects use include O

# print(df.info())

# print(df.isnull().sum())  #will give sum of null




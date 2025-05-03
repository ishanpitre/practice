import pandas as pd
#from csv
# data = pd.read_csv('Output.csv',names=['cust_name','cust_age','cust_city'],header=0)
# print(data)




# from excel
sheetNames = ['copper','silver','gold','diamond']
#excel_data = pd.read_excel('E:\coding playround\Data Engineering\Python Pandas\output.xlsx',sheet_name='gold')
temp_df = []
for i in sheetNames:
    temp_df.append(pd.read_excel('E:\coding playround\Data Engineering\Python Pandas\output.xlsx',sheet_name=i))
pd.concat(temp_df)
print(temp_df)



import pandas as pd
s=[10,20,30]#list in series
seriesData=pd.Series(s)
print(seriesData)

seriesData=pd.Series(s,index=["a","b","c"])
print(seriesData)

print(seriesData["a"]) #index

seriesData=pd.Series({"a":100,"b":200,"c":300}) #dictionaries in Series
print(seriesData)

data={
    "iphone":[10,15,20],
    "ipad":[2,3,4]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0]) #loc data frame
print(df.loc[[0,1]])

df=pd.DataFrame(data,index=["a","b","c"])
print(df)
print(df.loc["a"])

pf=pd.read_csv("sneha.csv")
print(pf)

print(pf.head()) #print 1st 5 records 0f line

print("+++++++")
print(pf.tail())#print last 5 records 0f line

print(pf.info()) #provides information

print(pf)

#pf.dropna( inplace=True) #clean  by removing null column whole row and updates the data
print(pf)

#pf.fillna("N/A",inplace=True)
print(pf)

#pf["sold_price"].fillna(0,inplace=True)
print(pf)
pf["sold_price"].fillna(0,inplace=True)
pf["product_name"].fillna("N/A",inplace=True)
pf["product_category"].fillna("N/A",inplace=True)
pf["sold_price"].fillna("N/A",inplace=True)

print(pf["sold_price"].mean())
print(pf["sold_price"].median())
print(pf["sold_price"].mode())
pf.loc[2,"product_name"]="boat chocolate"
print(pf)

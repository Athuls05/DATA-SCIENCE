import pandas as pd
a=pd.DataFrame.from_dict({
    "Name":["ammu","malu","nandhu"],
    "age":[20,30,50],
    "income":[2000,3000,6000]
})
print(a.head())
import pandas as pd 
import numpy as np
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder

customers_df=pd.read_csv("customers.csv")
orders_df=pd.read_csv("orders.csv")
products_df=pd.read_csv("products.csv")

print("Customer details:\n",customers_df)
print("Order details:\n",orders_df)
print("Product details:\n",products_df)

customers_df['age'].fillna(customers_df['age'].mean(),inplace=True)
customers_df['email'].fillna('NA', inplace=True)

merged_df=pd.merge(pd.merge(customers_df,orders_df,on='cid'),products_df,on='pid')
merged_df['total_price']=merged_df['quantity']*merged_df['price']
merged_df['feedback']=np.where(merged_df['quantity']>1,"Good","Bad")
print("\n Cleaned,integrated and transformed data\n",merged_df)

ordinal_encoder=OrdinalEncoder()
label_encoder=LabelEncoder()

x=merged_df.drop(columns=['feedback'])
y=merged_df['feedback']
categorical_cols=x.select_dtypes(include=['object']).columns

x[categorical_cols]=ordinal_encoder.fit_transform(x[categorical_cols])

y_encoded=label_encoder.fit_transform(y)

print("\nFeatures:\n",x)
print("\nTarget:\n",y_encoded)
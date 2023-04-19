#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#%%
df = pd.read_excel('/home/docker/ecommerce/ecom_analysis/ecom.xlsx', sheet_name='E Comm')
df_c = df[df['Churn'] == 1]
df_nc = df[df['Churn'] == 0]

# %%
df.describe()
#df_id = df.pop('CustomerID')
#churn_values = df.pop('Churn')


#%%
sns.countplot(x='Churn',data=df)
plt.title('No Churn vs Churned')
plt.xlabel('No Churn: 0  Vs  Churned: 1')
plt.ylabel('Count')

#%%
# select columns not object
df_cv = df.select_dtypes(exclude='object')
df_cat = df.select
#%%
# Density distribution plots  
 
fig, ax = plt.subplots(3,4,figsize=(20, 18))
fig.suptitle('Density of Numeric Features by Churn', fontsize=20)
ax = ax.flatten()

for idx,col in enumerate(df_cv.columns[2:]):
    sns.kdeplot(data=df_c[col], label='Churned', linewidth=3, ax=ax[idx] )
    sns.kdeplot(data=df_nc[col], label='No Churn', linewidth=3, ax=ax[idx])
    ax[idx].legend(loc='upper right')

plt.show()



#%%
df_id = df.pop('CustomerID')
churn_values = df.pop('Churn')
# %%
sns.jointplot(x=df_c['Tenure'], y = df_c['CouponUsed'], kind='kde', cmap='Blues')
#%%
sns.jointplot(x=df_nc['Tenure'], y = df_nc['CouponUsed'], kind='kde', cmap='Blues')



# %%

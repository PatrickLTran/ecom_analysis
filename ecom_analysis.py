#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%%
df = pd.read_excel('/home/docker/ecommerce/ecom.xlsx', sheet_name='E Comm')
df_c = df[df['Churn'] == 1]
df_nc = df[df['Churn'] == 0]

# %%
df.describe()
df_id = df.pop('CustomerID')
churn_values = df.pop('Churn')

df_churned = df.

#%%
sns.countplot(x='Churn',data=df,)
plt.title('No Churn vs Churned')
plt.xlabel('No Churn: 0  Vs  Churned: 1')
plt.ylabel('Count')

#%%
fig, ax = plt.subplots(3,4,figsize=(20, 18))
ax.flatten()
for i in df.columns[2:]:
    sns.kdeplot(data=df_c[i], label='Churned', linewidth=3)
    sns.kdeplot(data=df_nc[i], label='No Churn', linewidth=3)
    plt.xlabel(i)
    plt.ylabel('Density')
plt.show()



#%%
df_id = df.pop('CustomerID')
churn_values = df.pop('Churn')
# %%




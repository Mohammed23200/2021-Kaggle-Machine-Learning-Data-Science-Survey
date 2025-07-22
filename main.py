import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from itertools import cycle

data =pd.read_csv("kaggle_survey_2021_responses.csv")
qustions = data.iloc[0,:]
data.drop(index=0,inplace=True)
cust_color = [
    '#6ee1fa',
'#65d4ee',
'#5cc6e3',
'#54b9d7',
'#4caccb',
'#449fbf',
'#3c93b3',
'#3586a7',
'#2d7a9b',
'#266e8f',
'#1f6282',
'#175776',
'#104c6b',
'#07415f',
'#003653'
]

for col in data.columns:
    if data[col].str.isnumeric().all():
        data[col]=pd.to_numeric(data[col])
countries=data['Q3'].unique()
countries_str='Algeria, Bahrain, Comoros, Djibouti, Egypt, Iraq, Jordan, Kuwait, Lebanon, Libya, Mauritania, Morocco, Oman, Palestine, Qatar, Saudi Arabia, Somalia, Sudan, Syria, Tunisia, United Arab Emirates, Yemen'
arabic_countries=countries_str.split(', ')
data_arab=data[data['Q3'].isin(arabic_countries)]

#TODO: line plot for age Distribution
age_groups = data_arab['Q1'].value_counts().sort_index()
y = age_groups.values # Remove parentheses
x = age_groups.index  # Remove parentheses
plt.plot(x, y,color="red")
plt.title("Age Distribution")
plt.ylabel("Frequency")
plt.xlabel("Age Group")
plt.show()
#TODO:Country Distribution Bar 
country_group = data_arab['Q3'].value_counts().sort_index()
x = country_group.index
y = country_group.values
plt.bar(x,y,color="red")
plt.xlabel("Country")
plt.ylabel("Frequency")
plt.title("Country Distribution")
plt.show()
#TODO:Arab Kaggle users by programming Language Distribution
q7_columns = [col for col in data_arab.columns if col.startswith('Q7')]
dic_7 = dict()
for col in q7_columns:
    for lang in data_arab[col].dropna().unique():
        if lang not in dic_7:
            dic_7[lang] = 0
        dic_7[lang] += (data_arab[col] == lang).sum()
q7_ser = pd.Series(dic_7)
explode = [0.2] + [0]*(len(q7_ser)-1)
plt.figure(figsize=(10,10))
plt.pie(q7_ser, shadow=True, labels=q7_ser.index, explode=explode, autopct="%1.1f%%")
plt.legend(q7_ser.index)
plt.show()
#TODO:Programming Language Distribution Subplots 
 
top_q7 = q7_ser.sort_values(ascending=False)[:10]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Bar Chart
axes[0].bar(top_q7.index, top_q7.values, color=cust_color[:10])
axes[0].set_ylabel("Count")
axes[0].set_xlabel("Languages")
axes[0].tick_params(labelrotation=45, labelsize=10)
axes[0].patch.set_facecolor('#F2F2F2')
axes[0].grid(color=cust_color[0], alpha=0.5, linestyle='--')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Pie Chart
axes[1].pie(top_q7.values, labels=top_q7.index, autopct='%1.1f%%', startangle=90, colors=cust_color[:10])
axes[1].set_title("Pie Chart")

# Title and Show
plt.suptitle("Top 10 Programming Languages Among Arab Kaggle Users", fontsize=16)
fig.patch.set_facecolor('#F2F2F2')
plt.show()


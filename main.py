import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read data
data=pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

#EDA
print(data.head())
print(data.info())
print(data.describe())
print(data.duplicated().sum())

#data preprocessing
data['OrderDate'] = pd.to_datetime(data['Order Date'])
data.drop('Order Date', axis=1, inplace=True)

#Distribution of categories
sns.countplot(x='Sub-Category', data = data)
sns.set(rc={'figure.figsize':(12,5)})
plt.xticks(rotation=60)
plt.title('Count of SubCategory')
plt.show()

#Which is the best performing category
sns.countplot(x='Category',data=data,hue='Category')

#Which customer segment is the most profitable?
df1=pd.DataFrame(data.groupby(['Segment'])[['Profit']].mean())
sns.barplot(data = df1, x = df1.index, y = df1.Profit, palette = "Blues")
plt.title("Customer Segment Profitability")
plt.show()

#Which is the preferred Ship Mode?
df2=data[['Ship Mode','Profit','Sales']]
df2=df2.groupby(['Ship Mode']).sum().reset_index()
plt.bar(x=df2['Ship Mode'], height=df2['Sales'], color='skyblue')
plt.bar(x=df2['Ship Mode'], height=df2['Profit'], bottom=df2['Sales'], color='green')
plt.title("Sales & Profit Across Ship Modes", size=20, pad=20)
plt.legend(['Sales','Profit'])

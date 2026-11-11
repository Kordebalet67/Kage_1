import pandas as pd
import csv
import base64

pd.options.display.max_rows = 500
pd.options.display.max_columns = 10
df = pd.read_csv('kaggleton_1_data.csv')

def decode_column(column):
    return column.apply(lambda x: base64.b64decode(x.encode()).decode())

df = df.apply(decode_column)
# print(df[["f7", "target"]].shape)
# print(df)
print(df.groupby(['medicine']).mean())
target = df[df["target"].isin(['6'])]
print(target[["medicine", "instrument", "cabinet", "target"]])
# df['target'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# print(df.describe())
# print(df.all)

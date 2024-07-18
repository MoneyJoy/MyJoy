```python
import numpy as np
import pandas as pd

df = pd.read_excel("水质情况.xlsx", "Sheet1", engine="openpyxl")
# print(df.head(10))  # 前十行
# print(df)
arr = np.array([1, 3, 4])

date = {'样本号': [1, 2, 3], '萼片长': [4.5, 4.6, 6.4], '类型': [0, 0, 1]}
print(date)
datef = pd.DataFrame(date)
print(datef)

# 基础信息
print(df.head())
print(df.info())

# 缺失值处理
df = df.dropna()
df['类型'] = df['类型'].astype(float)   # 类型转换
print(df.info())
# 选择和过滤
print(df['类型'] == 1)

df_1 = df[df['类型'] == 1]
print(df_1)
print(df_1.info())

lb = np.mean(df['PH值']) - 3 * np.std(df['PH值'])
ub = np.mean(df['PH值']) + 3 * np.std(df['PH值'])
df_2 = df[(df['PH值'] >= lb) & (df['PH值'] <= ub)]
print(df_2)
print(df_2.info())

```


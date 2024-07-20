```python
import pandas as pd
import numpy as np
from scipy import linalg

# 读取数据
path = "example.xlsx"
Sheet = "Sheet2"
df = pd.read_excel(path, Sheet, usecols="A:C")

# 转换为 NumPy 数组
X = df.to_numpy()
print("原始数据 X:")
print(X)

# 标准化数据
X = (X - np.mean(X, axis=0)) / np.std(X, ddof=1, axis=0)

# 计算协方差矩阵
R = np.cov(X.T)

# 计算特征值和特征向量
eigenvalues, eigenvectors = linalg.eig(R)

# 将特征值按降序排列，并重新排序特征向量
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# 计算主成分贡献率和累积贡献率
contribution_rate = eigenvalues / np.sum(eigenvalues)
cum_contributin_rate = np.cumsum(contribution_rate)

print("特征值为: ")
print(eigenvalues)
print("贡献率为: ")
print(contribution_rate)
print("累计贡献率为: ")
print(cum_contributin_rate)
print("与特征值对应的特征向量矩阵为: ")
print(eigenvectors)

```


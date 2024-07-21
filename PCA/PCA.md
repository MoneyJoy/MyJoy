# 主成分分析

## 1. 原理

通过某个投影矩阵将高维空间的中的原始样本点线性投影到低维空间,以达到降维的目的

降维的几何意义可以理解为旋转坐标系,取前k个轴作为新特征

**将特征维度变小,同时减少信息损失**

**数据降维**

优点: 1. 是数据集更容易使用  2. 降噪声  3. 降低算法的计算开销  4. 使得结果更容易理解

- 换特征
- 减少特征

![image-20240720193044474](img\image-20240720193044474.png)

![image-20240720194544304](img\image-20240720194544304.png)

## 2. 代数意义

**m * n阶的原始样本X, 与n * k阶的矩阵W做矩阵乘法运算X * W, 即得到m * k阶低维矩阵Y, 这里的n * k阶矩阵W就是投影矩阵**

## 3. 思想

![image-20240720195204889](img/image-20240720195204889.png)

## 4. 计算步骤

![image-20240720195408337](img/image-20240720195408337.png)

![image-20240720195620686](img/image-20240720195620686.png)

![image-20240720195851444](img/image-20240720195851444.png)

![image-20240720200115450](img/image-20240720200115450.png)

## 5. 例题

![image-20240720200250892](img/image-20240720200250892.png)

![image-20240720200349732](img/image-20240720200349732.png)

![image-20240720201214860](img/image-20240720201214860.png)

## 6. 分析说明

![image-20240720201637954](img/image-20240720201637954.png)

## 7. 代码实现

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


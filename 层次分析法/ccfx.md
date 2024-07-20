```python
from fractions import Fraction
import numpy as np

# 从用户输入获取矩阵A的值
def get_matrix_input(n):
    print(f"请输入 {n}x{n} 矩阵的值，每行的值以空格分隔:")
    A = np.zeros((n, n))
    for i in range(n):
        row_input = input().split()
        A[i] = [float(Fraction(val)) for val in row_input]
    return A

n = int(input("请输入矩阵的维度:"))  # 假设矩阵的维度为4，你可以根据需要修改这个值
A = get_matrix_input(n)

eig_val, eig_vec = np.linalg.eig(A)  # eig_val是特征值, eig_vec是特征向量
Max_eig = max(eig_val)

CI = (Max_eig - n) / (n - 1)
RI = [0, 0.00001, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]

CR = CI / RI[n - 1]

print("一致性指标CI=", CI)
print("一致性比例CR=", CR)

if CR < 0.10:
    print("CR < 0.10,所以该判断矩阵的一致性可以接受")
    # 算术平均法求权重
    ASum = np.sum(A, axis=0)
    Stand_A = A / ASum
    ASumr = np.sum(Stand_A, axis=1)
    weights_arithmetic = ASumr / n
    print("算术平均法求权重:", weights_arithmetic)

    # 几何平均法求权重
    prod_A = np.prod(A, axis=1)
    prod_n_A = np.power(prod_A, 1 / n)
    re_prod_A = prod_n_A / np.sum(prod_n_A)
    print("几何平均法求权重:", re_prod_A)

    # 特征值法求权重
    max_index = np.argmax(eig_val)  # argmax用于返回数组中最大值的索引
    max_vec = eig_vec[:, max_index]
    weights_eigenvalue = max_vec / np.sum(max_vec)
    print("特征值法求权重:", weights_eigenvalue)
else:
    print("CR >= 0.10,所以该判断矩阵需要进行修改")
```


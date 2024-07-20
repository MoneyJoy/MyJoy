```python
import numpy as np
from fractions import Fraction

def min_to_max(max_value, x):
    """将极小型指标转化为极大型指标"""
    return max_value - np.array(x)


def mid_to_max(best_value, x):
    """将中间型指标转化为极大型指标"""
    h = np.abs(np.array(x) - best_value)
    M = max(h)
    if M == 0:
        M = 1
    return 1 - h / M


def reg_to_max(lower, upper, x):
    """将区间型指标转化为极大型指标"""
    x = np.array(x)
    M = max(lower - min(x), max(x) - upper)
    if M == 0:
        M = 1
    result = []
    for value in x:
        if value < lower:
            result.append(1 - (lower - value) / M)
        elif value > upper:
            result.append(1 - (value - upper) / M)
        else:
            result.append(1)
    return np.array(result)

def main():
    n = eval(input("请输入参评数目: "))
    m = eval(input("请输入指标数目: "))

    print("请输入该类型矩阵: 1:极大型 2:极小型 3:中间型 4:区间型")
    kind = input().split()

    print("请输入矩阵: ")
    A = np.zeros(shape=(n, m))
    for i in range(n):
        row = input().split()
        A[i] = [float(Fraction(val)) for val in row]
    print(f"输入的矩阵为: \n{A}")

    X = np.zeros((n, m))
    for i in range(m):
        column = A[:, i]
        if kind[i] == "1":
            X[:, i] = column
        elif kind[i] == "2":
            max_value = max(column)
            X[:, i] = min_to_max(max_value, column)
        elif kind[i] == "3":
            best_value = float(Fraction(input("类型三,请输入最优值: ")))
            X[:, i] = mid_to_max(best_value, column)
        elif kind[i] == "4":
            lower = float(Fraction(input("类型四, 请输入区间[a, b]值a: ")))
            upper = float(Fraction(input("类型四, 请输入区间[a, b]值b: ")))
            X[:, i] = reg_to_max(lower, upper, column)
    print(f"统一指标后矩阵为: \n{X}")

    # 对正向化后的矩阵进行预处理
    Mean = np.mean(X, axis=0)
    Z = X / Mean

    print("预处理后的矩阵为: ")
    print(Z)

    # 构造母序列和子序列
    Y = np.max(Z, axis=1)
    X = Z

    # 计算得分
    absX0_Xi = np.abs(X - np.tile(Y.reshape(-1, 1), (1, X.shape[1])))
    print(f"abs:   {absX0_Xi}")
    a = np.min(absX0_Xi)
    b = np.max(absX0_Xi)
    rho = 0.5
    gamma = (a + rho * b) / (absX0_Xi + rho * b)
    weight = np.mean(gamma, axis=0) / np.sum(np.mean(gamma, axis=0))
    print(f"weight:   {weight}")
    score = np.sum(X * np.tile(weight, (X.shape[0], 1)), axis=1)
    stand_S = score / np.sum(score)
    sorted_S = np.sort(stand_S)[::-1]
    index = np.argsort(stand_S)[::-1]
    index += 1

    print("归一化后的索引及其得分: ")

    # print(sorted_S)
    # print(index)
    for i in range(sorted_S.shape[0]):
        print(f"{index[i]}: {sorted_S[i]}")

if __name__ == "__main__":
    main()
```


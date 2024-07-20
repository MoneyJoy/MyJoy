```python
import numpy as np
from fractions import Fraction
import pandas as pd


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


def normalize(matrix):
    """对矩阵进行标准化处理"""
    for col in range(matrix.shape[1]):
        norm = np.linalg.norm(matrix[:, col])
        if norm == 0:
            norm = 1
        matrix[:, col] /= norm
    return matrix


def calculate_distances(matrix, x_max, x_min):
    """计算每个参评对象与最优和最劣情况的距离"""
    d_positive = np.linalg.norm(matrix - x_max, axis=1)
    d_negative = np.linalg.norm(matrix - x_min, axis=1)
    return d_positive, d_negative


def main():
    # print("请输入参评数目")
    # num_objects = int(input("请输入参评数目"))
    #
    # print("请输入指标数目")
    # num_criteria = int(input("请输入指标数目"))
    '''
    df = pd.read_excel("20条河流的水质情况数据.xlsx", "Sheet1")
    index = ['含氧量（ppm)', 'PH值', '细菌总数(个/mL)', '植物性营养物量（ppm)']
    new_df = df[index]
    '''
    new_df = pd.read_excel("kun_kun.xlsx", "Sheet1")
    # 将数据框转换为 NumPy 数组
    A = new_df.to_numpy()
    num_objects, num_criteria = A.shape

    print("请输入类型矩阵: 1:极大型, 2:极小型, 3:中间型, 4:区间型")
    criteria_types = input().split()

    # print("请输入矩阵")
    # A = np.zeros((num_objects, num_criteria))
    # for i in range(num_objects):
    #     row_input = input().split()
    #     A[i] = [float(Fraction(val)) for val in row_input]
    '''
    A = np.array(eval(input("请输入初始矩阵: ")))
    #格式: [[55,24,10],[35,38,22],[75,40,18],[100,50,20]]
    '''
    print(f"输入矩阵为: \n{A}")

    X = np.zeros(shape=(num_objects, num_criteria))
    for i in range(num_criteria):
        column = A[:, i]
        if criteria_types[i] == "1":
            X[:, i] = column
        elif criteria_types[i] == "2":
            max_value = max(column)
            X[:, i] = min_to_max(max_value, column)
        elif criteria_types[i] == "3":
            print("类型三,请输入最优值: ")
            best_value = float(Fraction(input()))
            X[:, i] = mid_to_max(best_value, column)
        elif criteria_types[i] == "4":
            print("类型四, 请输入区间[a, b]值a: ")
            lower = float(Fraction(input()))
            print("类型四, 请输入区间[a, b]值b: ")
            upper = float(Fraction(input()))
            X[:, i] = reg_to_max(lower, upper, column)
    print(f"统一指标后矩阵为: \n{X}")

    X = normalize(X)
    print("是否需要设置权重: 1:是  0:否")
    pan = int(input())
    if pan == 1:
        col = X.shape[1]
        print("请输入权重: ")
        row = input().split(" ")
        quan = np.array([float(Fraction(val)) for val in row])
        for i in range(col):
            X[:, i] = X[:, i] * quan[i]

    print(f"标准化矩阵为: \n{X}")

    x_max = np.max(X, axis=0)
    x_min = np.min(X, axis=0)
    print("每个指标的最大值: ", x_max)
    print("每个指标的最小值: ", x_min)

    d_positive, d_negative = calculate_distances(X, x_max, x_min)
    print("d+向量", d_positive)
    print("d-向量", d_negative)

    epsilon = 1e-10  # 添加一个小常数以避免除以零
    denominator = d_positive + d_negative + epsilon
    scores = d_negative / denominator
    scores = np.nan_to_num(scores)  # 将 NaN 转换为零
    total_score = sum(scores)
    if total_score == 0:
        print("总得分为零，无法计算百分比。")
        return
    scores = 100 * scores / total_score
    for i, score in enumerate(scores):
        print(f"第{i + 1}个标准化后百分制得分为: {score}")


if __name__ == "__main__":
    main()

```


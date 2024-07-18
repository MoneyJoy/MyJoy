```python
import numpy as np

print("请输入参评数目")
n = int(input())
print("请输入指标数目")
m = int(input())

print("请输入类型矩阵: 1:极大型, 2:极小型, 3:中间型, 4:区间型")
kind = input().split(" ")   # 将输入的字符串按空格分隔,形成列表

print("请输入矩阵")
A = np.zeros(shape=(n, m))  # 初始化一个n行m列的全零矩阵
for i in range(n):
    A[i] = input().split(" ")
    A[i] = list(map(float, A[i]))   # 将接收到的字符串列表转换为浮点数列表
print(f"输入矩阵为: \n{A}")

def min2max(maxx, x):
    x = list(x)
    ans = [[(maxx - e)] for e in x]
    return np.array(ans)

def mid2max(bestx, x):
    x = list(x)
    h = [abs(e - bestx) for e in x]
    M = max(h)
    if M == 0:
        M = 1
    ans = [[(1 - e / M)] for e in h]
    return np.array(ans)

def reg2max(lowx, highx, x):
    x = list(x)
    M = max(lowx - min(x), max(x) - highx)
    if M == 0:
        M = 1
    ans = []
    for i in range(len(x)):
        if x[i] < lowx:
            ans.append([(1-(lowx-x[i])/M)])
        elif x[i] > highx:
            ans.append([(1-(x[i]-highx)/M)])
        else:
            ans.append([1])
    return np.array(ans)

X = np.zeros(shape=(n, 1))
for i in range(m):
    if kind[i] == "1":
        v = np.array(A[:, i])
    elif kind[i] == "2":
        maxA = max(A[:, i])
        v = min2max(maxA, A[:, i])
    elif kind[i] == "3":
        print("类型三,请输入最优值: ")
        bestA = eval(input())
        v = mid2max(bestA, A[:, i])
    elif kind[i] == "4":
        print("类型四, 请输入区间[a, b]值a: ")
        lowA = eval(input())
        print("类型四, 请输入区间[a, b]值b: ")
        highA = eval(input())
        v = reg2max(lowA, highA, A[:, i])
    if i == 0:
        X = v.reshape(-1, 1)
    else:
        X = np.hstack([X, v.reshape(-1, 1)])    # 水平堆叠
print(f"统一指标后矩阵为: \n{X}")

# 对统一后的矩阵进行标准化处理
X = X.astype('float')
for j in range(m):
    X[:, j] = X[:, j]/np.sqrt(sum(X[:, j]**2))
print(f"标准化矩阵为: \n{X}")

# 最大值最小值距离的计算
x_max = np.max(X, axis=0)
x_min = np.min(X, axis=0)
d_z = np.sqrt(np.sum(np.square((X - np.tile(x_max, (n, 1)))), axis=1))  # 计算每个参评对象与最优情况的距离
d_f = np.sqrt(np.sum(np.square((X - np.tile(x_min, (n, 1)))), axis=1))  # 计算每个参评对象与最劣情况的距离
print("每个指标的最大值: ", x_max)
print("每个指标的最小值: ", x_min)
print("d+向量", d_z)
print("d-向量", d_f)

# 计算每个参评对象的得分排名
s = d_f/(d_z+d_f)
Score = 100 * s / sum(s)
for i in range(len(Score)):
    print(f"第{i+1}个标准化后百分制得分为, {Score[i]}")
```


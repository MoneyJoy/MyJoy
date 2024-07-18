```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 10)
y = np.sin(x)

# 画线
# plt.plot(x, y)
# plt.title("y = sin(x)")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# 画点
# plt.scatter(x, y, marker="*", c="r", label="数据点")
# plt.plot(x, y, linestyle="--", label="折线")
# plt.legend()
# plt.show()

# fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 设置图形大小
# axes[0].scatter(x, y, marker="*", c="r", label="数据点")
# axes[0].set_xlabel("x")
# axes[0].set_ylabel("y")
# axes[0].set_title("数据点")
# axes[0].legend()
#
# axes[1].plot(x, y, linestyle="--", label="折线")
# axes[1].set_xlabel("x")
# axes[1].set_ylabel("y")
# axes[1].set_title("拟合结果")
# axes[1].legend()
#
# plt.show()

x = [1, 2, 3]
y = [2, 4, 6]
plt.bar(x, y, label="sd")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
```


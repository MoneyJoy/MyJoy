```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))

arr = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]])
# print(arr)
# print(type(arr), arr.shape)
# print(arr[0:2])
arr.reshape(-1)
print(arr)
arr_re = arr.reshape(-1)
print(np.sort(arr_re))
# np.mean(arr)  平均数
# np.max(arr)   最大值
# np.min(arr)   最小值
# np.std(arr)   标准差
# np.sort(arr)  排序
# np.sum(arr)   求和
print(arr[arr > 2])
print(arr[(arr > 2) & (arr < 4)])
print(arr[(arr > 2) | (arr < 4)])

# 保存和导入

np.save("arr", arr)
arr = np.load("arr.npy")
```


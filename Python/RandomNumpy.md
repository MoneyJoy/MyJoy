```python
import numpy as np

np.random.seed(1)
print(np.random.rand())
print()

arr = np.random.randint(0, 100, 16).reshape(4, 4)
print(np.sum(arr[arr <= 10]))
```


```python
import numpy as np

import pandas as pd

data = {'name': ["张三", "李四", "王五", "老六", "赵七"],
        '身高': [175 for i in range(5)],
        '体重': [75 for i in range (5)],
        '成绩': list(np.random.randint(30, 90, 5))}
df = pd.DataFrame(data)
print(df)
print(df[df['成绩'] == np.max(df['成绩'])])
print("平均分是", np.mean(df['成绩']))
new_df = df[df['成绩'] < 60]
print("不及格的同学是:")
print(new_df)
```


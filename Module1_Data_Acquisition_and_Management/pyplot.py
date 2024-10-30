import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods= 1000))
ts = ts.cumsum()
print(ts)

plt.figure()
ts.plot()
plt.show()



from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# data = pd.read_csv('data-load-files.csv',header=None,)
# x = data[0]
# y = data[1]

x,y = np.loadtxt('data-load-files.csv', delimiter=',', unpack=True)
print(x,y)

plt.plot(x,y, label='Load data from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting chart')
plt.legend()
plt.tight_layout()
plt.show()

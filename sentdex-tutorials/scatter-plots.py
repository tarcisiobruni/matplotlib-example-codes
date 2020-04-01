import matplotlib.pyplot as plt
import random

x = random.sample(range(1, 30), 25)
y = random.sample(range(1, 30), 25)


plt.scatter(x,y,label="skitsScatter",color='k',marker="*")

plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
plt.legend()
plt.show()
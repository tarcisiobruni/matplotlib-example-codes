import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [8,7,9,8,6]
eating =   [3,1,4,2,1]
working =  [7,6,9,9,7]
playing =  [3,5,4,0,1]
running =  [2,2,2,1,1]

labels = [
    'sleeping',
    'eating',
    'working',
    'playing',
    'running'
]

colors = [
    '#357a96',
    '#354a96',
    '#513596',
    '#96354a',
    '#96357a',
]

plt.stackplot(days,sleeping,eating,working,playing,running,labels=labels,colors=colors)

plt.xlabel('x')
plt.xlabel('y')
plt.title('Amazing stack plot')
plt.legend()
plt.tight_layout()
plt.show()
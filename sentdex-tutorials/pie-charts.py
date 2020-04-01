from matplotlib import pyplot as plt

activities = [
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

slices = [1,2,3,4,5]

plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0,0,0.1,0,0),
        wedgeprops={'edgecolor': 'white'},
        autopct='%1.1f%%' )


plt.title('Amazing stack plot')

plt.tight_layout()
plt.show()
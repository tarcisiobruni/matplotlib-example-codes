import matplotlib.pyplot as plt
import random

### Bar Chart ###

# Generate 6 random numbers between 10 and 30
# x = random.sample(range(1, 30), 6)
# y = random.sample(range(1, 30), 6)

# x2 = random.sample(range(2, 30), 6)
# y2 = random.sample(range(2, 30), 6)

# plt.bar(x,y,label='Bars 1')
# plt.bar(x2,y2,label='Bars 2')

### Histograms ###

# ages = [22,55,62,45,21,22,43,67,88,34,56,66,78,39,64,33,44,61,27,89,33,91,45,9,10,8,11,16,16,7,13,13,16,65]
# bins = [0,10,20,30,40,50,60,70,80,90,100] #bins are interals to analyse distribution from data

# plt.hist(ages,bins=bins,edgecolor='black', histtype='bar')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting vars')
plt.tight_layout()
plt.show()

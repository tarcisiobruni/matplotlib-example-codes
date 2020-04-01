import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,6,7]

x2 = [5,2,8]
y2 = [7,1,2]

plt.plot(x,y,label='First Line')
plt.plot(x2,y2, label='Second line')

plt.xlabel('Plt Number')
plt.ylabel('Important var')

plt.title('Interesting graph\nCheck it out')

plt.legend()

plt.show()
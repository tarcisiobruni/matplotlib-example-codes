from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [50, 20, 20, 10]
# labels = ['Fifty', 'Twenty', 'Twenty', 'Tenth']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0,0,0,0.01,0]


plt.pie(slices, labels=labels, explode=explode,shadow=True, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title('My awesome pie chart')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

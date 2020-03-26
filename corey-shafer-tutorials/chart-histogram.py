import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# plt.hist(ages, bins=bins, edgecolor='black')

data = pd.read_csv('data-histogram.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10,20,30,40,50,60,70]

plt.hist(ages,bins=bins,edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

# axis vertical line
plt.axvline(median_age,color='red',label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of respondents')
plt.xlabel('Ages')
plt.ylabel('Total of respondents')

plt.tight_layout()

plt.show()


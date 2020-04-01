import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data-filling-area.csv')
ages = data['Age']
py_salaries = data['Python']
dev_salaries = data['All_Devs']
js_salaries = data['JavaScript']


fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1, sharex=True)

# fig1,ax1 = plt.subplots()
# fig2,ax2 = plt.subplots()

ax1.plot(ages,dev_salaries, label='All Devs', color="#444444", linestyle="--")

ax2.plot(ages,py_salaries, label='Python')
ax2.plot(ages,js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Media Salary by Age')
ax1.set_ylabel('Median Salary')

ax2.legend()
ax2.set_title('Media Salary by Age')
ax2.set_ylabel('Median Salary')

plt.tight_layout()

plt.show()

import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('./data-filling-area.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#008fd5', label="All Devs", linestyle="--")

plt.plot(ages, py_salaries, label="Python")

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25,where=(
    py_salaries > dev_salaries), interpolate=True, label="Above Avg")

plt.fill_between(ages, py_salaries, dev_salaries, alpha=0.25, where=(
    py_salaries <= dev_salaries), interpolate=True, color='#fc4f30', label="Bellow Avg")


plt.legend()
plt.title("Comparions between Devs Salaries Languages")
plt.xlabel('Age')
plt.xlabel('Salary Median (USD)')

plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

from matplotlib import pyplot as plt

plt.style.use('ggplot')

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels=['ply1','ply2','ply3']
colors = ['#008fd5','#fc4f30','#e5ae37']

plt.stackplot(minutes,player1, player2, player3, labels=labels,colors=colors)
plt.title('Awesome stack chart')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()


# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

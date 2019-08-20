import matplotlib.pyplot as plt

plt.title("Score graph")
plt.xlabel("Percent")
plt.ylabel("Score")
plt.plot([0,1,2,5,10,30,45,60,90,100], [100,97,87,79,67,45,42,30,23,19])

fig = plt.gcf()
fig.savefig('./fig1.png')

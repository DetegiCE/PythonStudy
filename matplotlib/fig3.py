import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothic'

plt.title("점수 그래프")
plt.xlabel("퍼센트")
plt.ylabel("점수")

plt.plot([0,1,2,5,10,30,45,60,90,100], [100,97,87,79,67,45,42,30,23,19])

fig = plt.gcf()
fig.savefig('./fig3.png')

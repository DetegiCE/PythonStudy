import matplotlib.pyplot as plt

route = './testbuff.png'

plt.axis('off')

plt.xlim(0,303)
plt.ylim(0,303)

plt.xticks([0,101,202,303])
plt.yticks([0,101,202,303])

stri = '010121010'

xst = [1,102,203,1,102,203,1,102,203]
yst = [203,203,203,102,102,102,1,1,1]

clr = ['#AAAAAA','#19FFFF','#FFFFFF']

for i in range(0,9):
        plt.gca().add_patch(plt.Rectangle((xst[i],yst[i]),100,100,fc=clr[int(stri[i])]))

hehe=[0,101,202,303]
hehl=[1,0.5,0.5,1]
for h in range(0,4):
        plt.axvline(x=hehe[h], color='#000000', linewidth=hehl[h])
        plt.axhline(y=hehe[h], color='#000000', linewidth=hehl[h])

plt.subplots_adjust(left=0,bottom=0,right=1,top=1,hspace=0,wspace=0)

fig = plt.gcf()
fig.set_size_inches(1,1)
fig.savefig(route, dpi=303)

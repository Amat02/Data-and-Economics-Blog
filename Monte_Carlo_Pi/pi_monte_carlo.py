#%%
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

z = 0

for i in range(1000,31000,1000):
    circle_points = 0
    square_points = 0
    iterations = 0
    z += 1
    abc=[];ordi=[];col=[]
    while iterations < i:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        d = x**2 + y**2
        if d <= 1:
            circle_points += 1
            col.append('red')
        else:
            col.append('blue')
        square_points += 1
        iterations += 1
        pi = (4*(circle_points/square_points))
        abc.append(x)
        ordi.append(y)
    
    fig1 = plt.figure(figsize=(5,5),dpi=250)
    ax = fig1.add_subplot(111)
    ax.scatter(abc,ordi,alpha=0.8,s=0.5,c=col)
    plt.xlim((-1,1));plt.ylim((-1,1))
    ax.add_patch(patches.Circle((0,0),radius=1,alpha=0.5, facecolor="white", edgecolor="black", linewidth=2, linestyle='solid'))
    plt.text(-0.985,1.015,'\u03C0 \u2248 '+str(round(pi,3)),fontsize=12)
    plt.text(0.53,1.015,'n = '+str(i),fontsize=12)
    if z < 10:
        file = 'pi00'+str(z)
    else:
        file = 'pi0'+str(z)
    plt.savefig(fname=file)

    
    
import numpy as np
pi=np.pi
X=[[[67/5,pi/2,0],[-14/5,11/7,-10],[2942/7,16/5,1],[43/5,39/10,2],[123/4,3/7,3],[10,3/5,4],
    [39/4,15/4,5],[44/7,49/12,6],[7/2,1,7],[29/7,8/7,8],[5/4,23/6,9]]+6*[[0,0,0]],
   [[-4019/4,pi/2,0],[-22/5,4/3,-8],[1841/6,19/7,1],[357/4,23/11,2],[106/3,4,3],[351/14,1/14,4],
    [127/8,22/7,5],[36/5,33/7,6],[91/18,22/9,7],[23/6,1/5,9],[17/6,9/2,10]]+6*[[0,0,0]],
   [[1198/3,pi/2,0],[-61/15,8/9,-8],[-51/5,4/3,-6],[1453/4,14/5,1],[614/7,13/6,2],[75/2,13/3,3],
    [122/5,1/16,4],[175/11,13/4,5],[19/4,9/5,7],[5,1/2,9],[13/7,4,10]]+6*[[0,0,0]],
   [[-13027/13,pi/2,0],[-14/3,2/5,-6],[-29/5,5/9,-5],[-37/4,1/3,-4],[3021/7,97/32,1],[179/9,34/11,2],
    [53/5,29/10,3],[1/2,18/5,7],[11/6,16/7,8],[11/5,7/3,9],[5/6,11/5,10]]+6*[[0,0,0]],
   [[785/2,pi/2,0],[-3/5,1/6,-10],[-23/7,2/7,-6],[-23/3,1/8,-5],[-10,1/5,-4],[2417/5,34/11,1],
    [89/4,16/5,2],[11/5,14/5,3],[31/16,17/6,7],[20/7,23/8,8],[17/7,11/4,9]]+6*[[0,0,0]],
   [[-1087/5,pi/2,0],[-2,4/3,-16],[-39/11,6/5,-14],[-21/4,14/9,-12],[-41/3,3/2,-6],
    [5028/5,23/12,1],[713/14,17/5,2],[103/3,7/3,3],[258/7,13/3,4],[142/13,1,5],[179/15,9/7,7],
    [17/3,13/3,8],[47/6,5/3,9],[90/13,22/5,10],[18/5,13/7,11],[18/5,7/5,13],[26/7,7/4,15]],
   [[-277/3,pi/2,0],[8875/6,28/9,1]]+15*[[0,0,0]],[[-467/5,pi/2,0],[4832/3,31/10,1]]+15*[[0,0,0]]]
Y=[[[-6393/7,pi/2,0],[-1/3,4/3,-10],[-21/22,3/5,-9],[-4,7/5,-5],[-21/4,1/4,-4],[4217/17,9/2,1],
    [74/3,15/7,2],[32/3,11/7,3],[7/4,16/5,6],[2,13/6,7],[4/5,2/3,8]]+6*[[0,0,0]],
   [[4843/9,pi/2,0],[-209/6,1/5,-4],[-249/8,6/5,-3],[577/2,40/9,1],[184/3,9/4,2],[83/7,2/3,5],
    [25/3,12/5,6],[5,17/6,7],[5/3,1/7,8],[23/6,1/4,9],[5/4,5/4,10]]+6*[[0,0,0]],
   [[5301/10,pi/2,0],[-131/4,4/5,-3],[1781/6,9/2,1],[422/7,9/4,2],[189/5,1/16,4],[79/6,8/5,5],
    [34/3,26/9,6],[22/5,23/7,7],[35/12,2/7,8],[11/4,5/7,9],[14/5,10/3,10]]+6*[[0,0,0]],
   [[2127/4,pi/2,0],[401,23/5,1],[118/3,7/5,2],[68/3,6/5,3],[133/8,6/5,4],[11/3,4/3,5],
    [24/7,57/14,6],[34/7,45/11,7],[25/7,37/9,8],[1/3,19/5,9],[9/5,3/5,10]]+6*[[0,0,0]],
   [[3688/7,pi/2,0],[13121/32,14/3,1],[44,10/7,2],[123/4,7/5,3],[15,4/3,4],[3/4,12/5,5],
    [27/5,13/3,6],[40/7,31/7,7],[13/6,13/3,8],[6/5,6/5,9],[58/19,1,10]]+6*[[0,0,0]],
   [[-9879/19,pi/2,0],[-19/7,8/7,-12],[-103/5,7/8,-5],[-80/9,11/7,-4],[3665/6,18/5,1],
    [803/6,13/5,2],[441/8,9/2,3],[17/2,4/5,6],[27/5,1/3,7],[17/3,2,8],[9/5,24/7,9],
    [15/4,26/7,10],[13/5,41/9,11],[16/17,1/5,13],[23/11,1/4,14],[7/4,25/12,15],[2/3,9/7,16]],
   [[1105/12,pi/2,0],[5913/4,14/3,1]]+15*[[0,0,0]],[[359/4,pi/2,0],[8012/5,14/3,1]]+15*[[0,0,0]]]
def unit_step(t):
    if t<0: return 0
    else: return 1
def bf(k,t): return k[0]*np.sin(k[1]+k[2]*t)
def us(j,t): return unit_step((31-4*j)*pi-t)*unit_step((-27+4*j)*pi+t)
def gus(t): return unit_step(np.sign(np.sin(t/2)))
def x(t): 
    return np.sum([np.sum([bf(X[j][i],t) for i in range(17)])*us(j,t) 
                   for j in range(8)])*gus(t)
def y(t): 
    return np.sum([np.sum([bf(Y[j][i],t) for i in range(17)])*us(j,t) 
                   for j in range(8)])*gus(t)
T=[np.linspace(.1**5,2*pi-.1**5,512)+2*pi*i for i in range(16)]
XT=[[x(T[i][j]) for j in range(512)] for i in range(16)]
YT=[[y(T[i][j]) for j in range(512)] for i in range(16)] 
import plotly.graph_objects as go
import numpy as np

a,b=np.random.randint(1,3),np.random.randint(3,5)
c,d=np.random.randint(2,4),np.random.randint(10,12)
e,f=np.random.randint(13,18),np.random.randint(1,3)
t=np.linspace(0,2*np.pi,60); r=[-1,0,1]
fx=-d*np.cos(t)-f*np.cos(b*t)+e*np.sin(a*t)
fy=-e*np.cos(a*t)+d*np.sin(t)-f*np.sin(b*t)
fz=d*np.cos(c*t)

fig=go.Figure(data=[go.Scatter3d(z=r[k]*fz,\
x=r[i]*fx,y=r[j]*fy,marker=dict(size=1.5)) \
for i in range(3) for j in range(3) for k in range(3)])
scene=dict(xaxis=dict(title='',showticklabels=False),
           yaxis=dict(title='',showticklabels=False),
           zaxis=dict(title='',showticklabels=False))
fig.update_layout(title='3D Functions',autosize=False,
                  width=500,height=500,showlegend=False,
                  margin=dict(l=3,r=3,b=3,t=30),
                  scene=scene,template='plotly_dark')
fig.show()
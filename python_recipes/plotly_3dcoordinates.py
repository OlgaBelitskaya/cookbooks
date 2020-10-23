import plotly.graph_objects as go
import numpy as np

fpath='../input/image-examples-for-mixed-styles/'
b=np.loadtxt(fpath+'beethoven.csv',delimiter=',',skiprows=1)

fig=go.Figure(data=[go.Scatter3d(x=b[:,0],y=b[:,1],z=b[:,2],\
mode='markers',marker=dict(size=.9,color='green')) \
for i in range(3) for j in range(3) for k in range(3)])
scene=dict(xaxis=dict(title='',visible=False),
           yaxis=dict(title='',visible=False),
           zaxis=dict(title='',visible=False))
fig.update_layout(title='3D Coordinates',autosize=False,
                  width=500,height=500,showlegend=False,
                  margin=dict(l=3,r=3,b=3,t=30),
                  scene=scene,template='plotly_dark')
fig.show()

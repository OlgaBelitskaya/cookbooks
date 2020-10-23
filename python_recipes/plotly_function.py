import plotly.graph_objects as go
import numpy as np

t=np.linspace(0,2*np.pi,3600) 
fig=go.Figure(); steps=[]
for step in np.arange(1,41,4):
    f=np.cos(14*t)+np.cos(6*t)
    fig.add_trace(go.Scatter(
            visible=False,name="k="+str(step),
            line=dict(color='rgb(.7,0,%f)'%(step/41),width=2),
            x=f*np.cos(step*t),y=f*np.sin(step*t)))
fig.data[0].visible=True
st="x=(cos(14t)+sin(6t))cos(kt) \n"+\
   "y=(cos(14t)+sin(6t))sin(kt)"
for i in range(len(fig.data)):
    step=dict(method="update",
              args=[{"visible":[False]*len(fig.data)}])
    step["args"][0]["visible"][i]=True
    steps.append(step)
sliders=[dict(active=10,pad={"t":20},steps=steps)]
fig.update_layout(width=500,height=550,sliders=sliders,
                  template='plotly_dark',
                  title_text=st,title_font=dict(size=15))
fig.show()
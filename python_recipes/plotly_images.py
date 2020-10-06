import os,numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from skimage import io
def plotly_images(file_path):
    files=os.listdir(file_path)
    numbers=np.random.randint(1,len(files),5)
    fig=make_subplots(1,5); steps=[]
    for step in np.arange(1,6,1):
        img=io.imread(file_path+files[numbers[step-1]])
        img=img[:,:,:3]
        fig.add_trace(go.Image(z=img),1,step)
        fig.data[step-1].visible=False
    fig.data[0].visible=True
    for i in range(len(fig.data)):
        step=dict(method="update",
                  args=[{"visible":[False]*len(fig.data)}])
        step["args"][0]["visible"][i]=True
        steps.append(step)
    sliders=[dict(active=0,pad={"t":5},steps=steps)]
    fig.update_layout(width=500,height=250,
                      sliders=sliders,
                      template='plotly_dark',
                      title_text="Image Examples",
                      title_font=dict(size=12))
    fig.update_xaxes(showticklabels=False)\
    .update_yaxes(showticklabels=False)
    return fig
#fig.show()
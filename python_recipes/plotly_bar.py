import pandas as pd
import plotly.express as px

values=['Fresh','Milk','Grocery','Frozen',
        'Detergents_Paper','Delicatessen']
customers=['Customer 1','Customer 2','Customer 3']
data=[[26373,36423,22019,5154,4337,16523],
      [16165,4230,7595,201,4003,57],
      [14276,803,3045,485,100,518]]
df=pd.DataFrame(data).T 
df.columns=customers; df.index=values

fig=px.bar(df,y='Customer 1',x=df.index,
           text='Customer 1',color=df.index)
fig.update_traces(texttemplate='%{text:d}',
                  textposition='outside')
fig.update_layout(width=500,height=500,
                  showlegend=False,
                  xaxis=dict(title=''))
fig.show()
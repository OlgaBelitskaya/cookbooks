import pandas as pd
import plotly.graph_objects as go

values=['Fresh','Milk','Grocery','Frozen',
        'Detergents_Paper','Delicatessen']
customers=['Customer 1','Customer 2','Customer 3']
data=[[26373,36423,22019,5154,4337,16523],
      [16165,4230,7595,201,4003,57],
      [14276,803,3045,485,100,518]]
df=pd.DataFrame(data).T 
df.columns=customers; df.index=values

pdata=[go.Bar(name=df.columns[i],
              x=df.index,y=df.iloc[:,i])
       for i in range(3)]
fig=go.Figure(pdata)
fig.update_layout(width=500,height=500,
                  barmode='stack',
                  template='plotly_white')
fig.show()
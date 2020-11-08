import os,pylab as pl,pandas as pd
from IPython.core.display import display,HTML

pl.style.use('seaborn-whitegrid')

def pandas_history(fit_history,csv=False):
    keys=list(fit_history.history.keys())
    list_history=[fit_history.history[keys[i]] 
                  for i in range(len(keys))]
    df_history=pd.DataFrame(list_history).T
    df_history.columns=keys
    if csv: 
        df_history.to_csv('df_history.csv',
                          index=False)
    return df_history 
    
def keras_history_plot(fit_history,fig_size=10,
                       col1='#00ff66',col2='#6600ff',
                       start=None,end=None):
    df_history=pandas_history(fit_history)
    if start==None: start=0
    if end==None: end=df_history.shape[0]
    fig=pl.figure(figsize=(fig_size,int(1.5*fig_size)))
    ax1=fig.add_subplot(311)
    df_history.iloc[start:end,[0,2]].plot(
        ax=ax1,color=[col1,col2])
    ax2=fig.add_subplot(312)
    df_history.iloc[start:end,[1,3]].plot(
        ax=ax2,color=[col1,col2])
    ax3=fig.add_subplot(313)
    df_history.iloc[start:end,4].plot(
        ax=ax3,color=col1)
    pl.legend(); pl.show();
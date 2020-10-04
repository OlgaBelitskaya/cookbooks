import pylab as pl,pandas as pd
pl.style.use('seaborn-whitegrid')
def keras_history_plot(fit_history,fig_size,color):
    keys=list(fit_history.history.keys())
    list_history=[fit_history.history[keys[i]] 
                  for i in range(len(keys))]
    dfkeys=pd.DataFrame(list_history).T
    dfkeys.columns=keys
    fig=pl.figure(figsize=(fig_size,fig_size))
    ax1=fig.add_subplot(311)
    dfkeys.iloc[:,[0,2]].plot(
        ax=ax1,color=['slategray',color])
    ax2=fig.add_subplot(312)
    dfkeys.iloc[:,4].plot(ax=ax2,color=color)
    pl.legend()
    ax3=fig.add_subplot(313)
    dfkeys.iloc[:,[1,3]].plot(
        ax=ax3,color=['slategray',color])
    pl.show();
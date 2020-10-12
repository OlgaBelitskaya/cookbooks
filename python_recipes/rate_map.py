import pandas as pd,pylab as pl
def rate_map(cmap):
    fp='https://data.cityofnewyork.us/resource/'
    se=pd.read_json(fp+'h7rb-945c.json')
    fl=['graduation_rate','attendance_rate',
        'latitude','longitude']
    se=se[fl].dropna()
    f,ax=pl.subplots(ncols=2,figsize=(10,5),
                     sharey=True)
    f=pl.gcf()
    for i in range(2):
        se[fl[i]]=se[fl[i]].astype('string')\
        .str.replace('N/A','0').astype('float')
        se.plot(kind='scatter',ax=ax[i],
            x='longitude',y='latitude',
            s=10,c=fl[i],alpha=.8,grid=True,
            title=fl[i].replace('_',' '),
            cmap=pl.get_cmap(cmap))
        ax[i].set_facecolor('slategray')
        cax=f.get_axes()[i+2]
        cax.set_ylabel('')
    pl.show()
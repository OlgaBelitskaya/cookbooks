import pandas as pd,pylab as pl
fp='https://data.cityofnewyork.us/resource/'
se=pd.read_json(fp+'h7rb-945c.json')
fl=['graduation_rate','attendance_rate',
    'latitude','longitude']
se=se[fl].dropna()
f,ax=pl.subplots(ncols=2,figsize=(11,4))
def rate_map(cmap):
    for i in range(2):
        se[fl[i]]=se[fl[i]].astype('string')\
        .str.replace('N/A','0').astype('float')
        se.plot(kind='scatter',
            x='longitude',y='latitude',
            s=10,c=fl[i],
            cmap=pl.get_cmap(cmap),
            title=fl[i].replace('_',' '),
        ax=ax[i],alpha=.8,grid=True)
        ax[i].set_facecolor('slategray')
    pl.show()
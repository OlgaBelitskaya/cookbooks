import numpy as np,pylab as pl,urllib
from scipy.io import wavfile
url='https://ccrma.stanford.edu/~jos/wav/'
file='slideflute.wav'
def amplitude_wavfile(url=url,file=file,fig_size=7,
	                  color1='#3636ff',color2='#ff36ff'):
    input_file=urllib.request.urlopen(url+file)
    output_file=open(file,'wb')
    output_file.write(input_file.read())
    output_file.close(); input_file.close()
    sr,wav=wavfile.read(file);
    wav=wav.astype('float')/np.iinfo(np.int16).max
    f,ax=pl.subplots(1,figsize=(fig_size,fig_size))
    ax.plot(wav[:,1],c=color1,lw=.05)
    ax.plot(wav[:,0],c=color2,lw=.05,alpha=.7)
    ax.set_ylabel('amplitude')
    pl.grid(); pl.show()
amplitude_wavfile()
import numpy as np,pylab as plot,urllib
from scipy.io import wavfile
url='https://ccrma.stanford.edu/~jos/'+\
    'wav/slideflute.wav'
input_file=urllib.request.urlopen(url)
output_file=open('slideflute.wav','wb')
output_file.write(input_file.read())
output_file.close(); input_file.close()
sr,wav=wavfile.read('slideflute.wav');
wav=wav.astype('float')/np.iinfo(np.int16).max
f,ax=pl.subplots(1,figsize=(7,5))
ax.plot(wav[:,1],c='#3636ff',lw=.05)
ax.plot(wav[:,0],c='#ff36ff',lw=.05,alpha=.7)
ax.set_ylabel('amplitude')
pl.grid(); pl.show()
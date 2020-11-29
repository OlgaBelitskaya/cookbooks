library(IRdisplay); library(reticulate)
library(imager); library(ggplot2); library(reshape2)
pl<-c('matplotlib','seaborn','pandas','networkx',
      'tensorflow','sklearn','h5py')
for (p in pl) {py_install(p)} 
np<-import('numpy'); pd<-import('pandas')
pl<-import('pylab'); sn<-import('seaborn')
sl<-import('sklearn'); tf<-import('tensorflow')
h5<-import('h5py'); nx<-import('networkx')

library(IRdisplay); library(reticulate); library(keras)
library(imager); library(ggplot2); library(reshape2)
library(magrittr); library(VennDiagram); library(igraph)

pl<-c('matplotlib','seaborn','pandas','networkx',
      'tensorflow','sklearn','h5py','scikit-image',
      'matplotlib_venn')
for (p in pl) {py_install(p)} 
np<-import('numpy'); pd<-import('pandas')
pl<-import('pylab'); sn<-import('seaborn')
sl<-import('sklearn'); tf<-import('tensorflow')
h5<-import('h5py'); nx<-import('networkx')
sm<-import('skimage')
mp3d<-import('mpl_toolkits.mplot3d')
ml<-import('matplotlib.lines')
venn<-import('matplotlib_venn')

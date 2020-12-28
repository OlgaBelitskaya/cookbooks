
library(keras)
display_keras_history<-function(history) {
    options(repr.plot.width=6,repr.plot.height=4,warn=-1)
    theme<-ggplot2::theme_grey()
    scale_fill<-ggplot2::scale_fill_manual(
        values=c('slategray','#ff355e'))
    scale_color<-ggplot2::scale_color_manual(
        values=c('slategray','#ff355e'))
    plot(history,metrics=c('loss','acc','lr'))+
    scale_fill+scale_color+theme }


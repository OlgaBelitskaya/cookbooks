
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='slategray')
cols<-c('#33ff33','#3333ff','#ffff33','#ff3333')
venn.plot<-draw.quad.venn(
    area1=31,area2=31,area3=31,area4=31,
    n12=11,n13=11,n14=11,n23=11,n24=11,n34=11,
    n123=2,n124=5,n134=2,n234=5,n1234=1,
    category=c('A','B','C','D'),
    fill=cols,cat.col=cols,cat.cex=3)


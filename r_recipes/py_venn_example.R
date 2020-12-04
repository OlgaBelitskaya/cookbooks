
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='white')
pl$figure(figsize=c(10,10))
v=venn$venn2(subsets=c(5,7,3),set_labels=c('A','B'))
v$get_label_by_id('10')$set_text('A & ¬B')
v$get_label_by_id('01')$set_text('B & ¬A')
v$get_label_by_id('11')$set_text('A & B')
v$get_patch_by_id('10')$set_color('slategray')
v$get_patch_by_id('01')$set_color('#3399ff')
v$get_patch_by_id('11')$set_color('steelblue')
for (text in v$set_labels){text$set_fontsize(20)}
for (text in v$subset_labels){text$set_fontsize(20)}
file_name_out<-paste0(
    'rpy_plot',sample(1:9999999,1),'.png')
pl$savefig(file_name_out)
im<-load.image(file_name_out)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)


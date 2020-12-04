
image_contour<-function(file_name) {
    options(repr.plot.width=10,repr.plot.height=10,
            repr.plot.bg='white')
    example<-load.image(file_name); de<-dim(example)
    example<-array_reshape(example,c(de[1],de[2],de[4]))
    gray_example<-sm$color$colorconv$rgb2grey(example)
    contours<-sm$measure$find_contours(gray_example,.85)
    pl$figure(figsize=c(9,8)); pl$gca()$invert_yaxis()
    for (i in 1:length(contours)) {
        pl$plot(contours[[i]][,1],contours[[i]][,2],lw=1)}
    pl$grid()
    file_name_out<-paste0(
        'rpy_plot',sample(1:9999999,1),'.png')
    pl$savefig(file_name_out)
    im<-load.image(file_name_out)
    par(mar=c(0,0,0,0)); plot(im,axes=FALSE)}


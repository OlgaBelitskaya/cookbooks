
file_path<-paste0('../input/flower-color-images/',
                  'flower_images/flower_images/')
img_path<-paste0(file_path,'0001.png')
img<-keras::image_load(img_path,target_size=c(128,128))
img<-keras::image_to_array(img)/255
im<-imager::load.image(img_path)
str<-c('keras: ',dim(img),'; imager: ',dim(im))
cat(paste0(str,collapse=' '))
options(repr.plot.width=6,repr.plot.height=6)
par(mar=c(2,2,2,2),mfrow=c(2,2))
plot(im,axes=FALSE); plot(as.raster(img))
gray_img<-keras::image_load(
    img_path,target_size=c(128,128),grayscale=TRUE)
gray_img<-keras::image_to_array(gray_img)/255
gray_img<-keras::array_reshape(gray_img,c(128,128))
cat(paste0(c('keras grayscale: ',dim(gray_img))))
image(c(1:128),c(1:128),gray_img,
      col=grey(seq(0,1,length=256)))

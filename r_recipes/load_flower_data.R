
file_path<-paste0('../input/flower-color-images/',
                  'flower_images/flower_images')
flowers<-read.csv(paste0(file_path,'/flower_labels.csv'))
n<-nrow(flowers)
flower_labels<-as.matrix(flowers['label'])
image_paths<-list.files(
    file_path,recursive=TRUE,full.names=TRUE)
image_paths<-image_paths[1:(length(image_paths)-1)]
image_loading<-function(image_path) {
    image<-keras::image_load(image_path,target_size=c(128,128))
    image<-keras::image_to_array(image)/255
    image<-keras::array_reshape(image,c(1,dim(image)))
    return(image) }
flower_images<-lapply(image_paths,image_loading)
flower_images<-keras::array_reshape(
    flower_images,c(-1,128,128,3))
print(paste0(c('image array: ',dim(flower_images),
             '; label array: ',dim(flower_labels)),
             collapse=' ')); cat('

')
print(tail(image_paths)); cat('

')
print(t(head(flowers)))

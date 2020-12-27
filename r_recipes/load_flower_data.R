
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
print(t(head(flowers))); cat('

')
dd<-c(-1,128*128*3); indices<-sample(1:n)
train_indices<-indices[1:round(.7*n)]
valid_indices<-indices[(round(.7*n)+1):round(.85*n)]
test_indices<-indices[(round(.85*n)+1):n]
flower_images<-keras::array_reshape(flower_images,dd)
x_train<-flower_images[train_indices,]
x_train<-keras::array_reshape(x_train,c(-1,128,128,3))
y_train<-flower_labels[train_indices]
x_valid<-flower_images[valid_indices,]
x_valid<-keras::array_reshape(x_valid,c(-1,128,128,3))
y_valid<-flower_labels[valid_indices]
x_test<-flower_images[test_indices,]
x_test<-keras::array_reshape(x_test,c(-1,128,128,3))
y_test<-flower_labels[test_indices]
print(paste0(c('processed image arrays: ',dim(x_train),', ',
               dim(x_valid),', ',dim(x_test)),collapse=' '))
print(paste0(c('processed label arrays: ',length(y_train),', ',
               length(y_valid),', ',length(y_test)),
             collapse=' '))


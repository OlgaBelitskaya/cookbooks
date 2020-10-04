import numpy as np,ast,cv2
import tensorflow as tf

def get_line(x1,y1,x2,y2):
    steep=abs(y2-y1)>abs(x2-x1); rev=False
    if steep: [x1,y1,x2,y2]=[y1,x1,y2,x2]
    if x1>x2:
        [x1,x2,y1,y2]=[x2,x1,y2,y1]; rev=True
    dx=x2-x1; dy=abs(y2-y1); error=int(dx/2)
    xy=[]; y=y1; ystep=None
    if y1<y2: ystep=1
    else: ystep=-1
    for x in range(x1,x2+1):
        if steep: xy.append([y,x])
        else: xy.append([x,y])
        error-=dy
        if error<0: y+=ystep; error+=dx
    if rev: xy.reverse()
    return xy

def get_image(data,target_size):
    data=ast.literal_eval(data)
    img_size=int(1.25*max(np.amax(data)))
    img=np.zeros((img_size,img_size))
    d=round(.1*img_size)
    for [x,y] in data:
        for i in range(len(x)):
            img[y[i]+d][x[i]+d]=1
            if (i<len(x)-1): 
                x1,y1,x2,y2=x[i],y[i],x[i+1],y[i+1]
            else: 
                x1,y1,x2,y2=x[i],y[i],x[0],y[0]
            for [xl,yl] in get_line(x1,y1,x2,y2): 
                img[yl+d][xl+d]=1
    img=img.reshape(img_size,img_size,1)    
    img=tf.image.resize(
        img,(target_size,target_size)).numpy()       
    return np.squeeze(img)

def cv_get_image(data,target_size,
                 lw=5,time_color=True):
    data=ast.literal_eval(data)
    img_size=int(1.25*max(np.amax(data)))
    img=np.zeros((img_size,img_size),dtype=np.int8)
    d=round(.1*img_size)
    for t,s in enumerate(data):
        for i in range(len(s[0])-1):
            color=255-min(t,10)*15 if time_color else 255
            _=cv2.line(img,
                       (s[0][i]+d,s[1][i]+d),
                       (s[0][i+1]+d,s[1][i+1]+d),
                       color,lw) 
    img=img.reshape(img_size,img_size,1)    
    img=tf.image.resize(
        img,(target_size,target_size)).numpy()       
    return np.squeeze(img)
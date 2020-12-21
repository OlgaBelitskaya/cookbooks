import imageio,numpy as np,pylab as pl
from skimage.transform import resize
from IPython.display import display,HTML

def artificial_image(
    img_size_out,num_points=7200,img_size=1024):
    a=(.5+.1**6*np.random.randint(1,999999))*\
      np.random.choice([-1,1],1)[0]
    b=np.random.randint(3,10)
    c=.1**3*np.random.randint(1,99)*\
      np.random.choice([-1,1],1)[0]
    t=np.arange(0,12*np.pi,1/num_points)
    fx=np.sin(t/6)+a*np.sin(b*t)*np.cos(t)-\
       c*np.sin(16*b*t)
    fy=np.cos(t/6)+a*np.sin(b*t)*np.sin(t)-\
       c*np.cos(16*b*t)
    fx=.951*(fx-1.051*fx.min())/(fx.max()-fx.min())
    fy=.951*(fy-1.051*fy.min())/(fy.max()-fy.min())
    fx=np.array(np.clip(fx*img_size,0,img_size),
                dtype='int32')
    fy=np.array(np.clip(fy*img_size,0,img_size),
                dtype='int32')
    f=np.array([[fx[i],fy[i]] for i in range(len(t))])
    img=np.ones((img_size,img_size,3))
    randcol=.9-.8*np.random.random(3)
    for [x,y] in f: img[y,x,:]=randcol
    img=resize(img,(img_size_out,img_size_out))
    return img,np.around(a,6),b,np.around(c,3),randcol

def artificial_image_display(
    img_size_out,fig_size=8,num_points=7200,img_size=1024):
    fig=pl.figure(figsize=(fig_size,fig_size))
    img,a,b,c,col=\
    artificial_image(img_size_out,num_points,img_size)
    ax=fig.add_subplot(1,1,1)
    pl.imshow(img); pl.axis('off');
    pl.title(str([a,b,c]),color=col)
    pl.tight_layout(); pl.show()

def artificial_image_animate(
    img_size_out,steps,fig_size=500,num_points=7200,img_size=1024):
    [img1,img2]=[artificial_image(
        img_size_out,num_points,img_size)[0] for i in range(2)]
    img1norm=np.linalg.norm(img1)
    img2norm=np.linalg.norm(img2)
    img2normalized=img2*(img1norm/img2norm)
    vectors12=[]
    for step in range(steps):
        interpolated=img1+(img2normalized-img1)*step/(steps-int(1))
        interpolated_norm=np.linalg.norm(interpolated)
        interpolated_normalized=\
        interpolated*(img1norm/interpolated_norm)
        vectors12.append(interpolated_normalized)
    vectors12=np.array(vectors12)
    img1normalized=img1*(img2norm/img1norm)
    vectors21=[]
    for step in range(steps):
        interpolated=img2+(img1normalized-img2)*step/(steps-int(1))
        interpolated_norm=np.linalg.norm(interpolated)
        interpolated_normalized=\
        interpolated*(img2norm/interpolated_norm)
        vectors21.append(interpolated_normalized)
    vectors212=np.array(vectors21)
    images=np.vstack([vectors12,vectors21])
    file_name='pic'+str(np.random.randint(1,99999,1)[0])+'.gif'
    imageio.mimsave(file_name,images)
    s1='<div id="imgs"><img src="'
    s2,s3,s4='" height="','" width="','"></img></div>'
    display(HTML(s1+file_name+s2+str(fig_size)+s3+str(fig_size)+s4))
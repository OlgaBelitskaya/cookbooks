import numpy as np,pylab as pl
import os,zipfile,cv2

def get_files(dir_name,files_pre):
    files_list=sorted(os.listdir(dir_name))
    input_files=[f for f in files_list 
                 if (f[-4:]=='.jpg' and files_pre==f[:-7])]
    return input_files

def get_edges(file):
    img=cv2.imread(file)   
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray_img,10,110) 
    cv2.waitKey(0)
    return img,gray_img,edges

def get_closed(edges):
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7)) 
    closed=cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel) 
    cv2.waitKey(0)
    return closed

def get_contours(gray_img,closed):
    (contours, _)=cv2.findContours(
        closed.copy(),cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    for c in contours: 
        arc=cv2.arcLength(c,True) 
        approx_pdp=cv2.approxPolyDP(c,.02*arc,True) 
        contours_img=cv2.drawContours(
            gray_img,[approx_pdp],-1,(0,255,0),2) 
    cv2.waitKey(0) 
    return contours,contours_img

def check_image(img):
    output=True
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray_img,10,150)        
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7)) 
    closed=cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
    (contours, _)=cv2.findContours(
        closed.copy(),cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE) 
    cv2.waitKey(0)
    cond1=(min(img.shape[0],img.shape[1])<30)
    cond2=(len(contours)!=1)
    cond3=(img.mean()<45 or img.mean()>250)
    if (cond1 or cond2 or cond3):
        output=False
    return output

def create_zip(img_list,contours_list,files_pre_list):
    files_list_out=[]
    N=len(files_pre_list)
    for l in range(N):
        start=files_pre_list[l].find('0')
        file_name_zip=files_pre_list[l][start:]+'.zip'
        idx=0
        for i in range(len(img_list[l])):
            contours=contours_list[l][i]
            img=img_list[l][i]
            for c in contours: 
                x,y,w,h=cv2.boundingRect(c)
                m=np.random.randint(5,21)
                if (w>30 and w<250 and h>30 and h<250):
                    y1=int(y*(1-.001*m))
                    y2=int((y+h)*(1+.001*m))
                    x1=int(x*(1-.001*m))
                    x2=int((x+w)*(1+.001*m))
                    new_img=img[y1:y2,x1:x2]
                    if check_image(new_img):
                        new_img=cv2.resize(new_img,(32,32))
                        file_name=files_pre_list[l][start:]+\
                                  '_%03d'%idx+'.png'
                        cv2.imwrite(file_name,new_img)
                        if idx==0:
                            with zipfile.ZipFile(file_name_zip,'w') as f:
                                f.write(file_name)
                        else:
                            with zipfile.ZipFile(file_name_zip,'a') as f:
                                f.write(file_name)
                        os.remove(file_name)
                        idx+=1 
        with zipfile.ZipFile(file_name_zip,'r') as f:
            curr_file_list_out=(f.namelist())
            f.close()
            files_list_out+=[curr_file_list_out]
    return files_list_out

dir_name='../input/object-detection/'
files_pre_list=['letters_01_'+'%02d'%l+'_00' 
                for l in range(2)]

def many_objects2images(dir_name=dir_name,
                        files_pre_list=files_pre_list):
    N=len(files_pre_list)
    input_files_list=[]
    input_files_list+=\
    [get_files(dir_name,files_pre_list[l])
     for l in range(N)]
    img_list,gray_img_list,edges_list=[],[],[]
    for l in range(N):
        curr_img_list=[]
        curr_gray_img_list=[]
        curr_edges_list=[]
        for i in range(len(input_files_list[l])):        
            img,gray_img,edges=\
            get_edges(dir_name+input_files_list[l][i])
            curr_img_list+=[img]
            curr_gray_img_list+=[gray_img]
            curr_edges_list+=[edges]
        img_list+=[curr_img_list]
        gray_img_list+=[curr_gray_img_list]
        edges_list+=[curr_edges_list]
    closed_list=[]
    for l in range(N):
        curr_closed_list=[]
        for i in range(len(input_files_list[l])):
            closed=get_closed(edges_list[l][i])
            curr_closed_list+=[closed]
        closed_list+=[curr_closed_list] 
    contours_list,contours_img_list=[],[]
    for l in range(N):
        curr_contours_list,curr_contours_img_list=[],[]
        for i in range(len(input_files_list[l])):
            contours,contours_img=\
            get_contours(gray_img_list[l][i],
                         closed_list[l][i])
            curr_contours_list+=[contours]
            curr_contours_img_list+=[contours_img]
        contours_list+=[curr_contours_list]
        contours_img_list+=[curr_contours_img_list]
    files_list_out=create_zip(
        img_list,contours_list,files_pre_list)
    print('Numbers of Images in Zip Files:\n',
          [len(files_list_out[l]) 
           for l in range(N)])
# -*- coding: utf-8 -*-
import  requests
import PIL.Image as Image


def image_joint(image_list,opt):#opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num=len(image_list)
    image_size=image_list[0].size
    height=image_size[1]
    width=image_size[0]
    
    if opt=='vertical':
        new_img=Image.new('RGB',(width,image_num*height),255)
    else:
        new_img=Image.new('RGB',(image_num*width,height),255)
    x=y=0
    count=0
    for img in image_list:
        
        new_img.paste(img,(x,y))
        count+=1
        if opt=='horizontal':
            x+=width
        else : y+=height
    return new_img

def wirtePicture(x, y):    
    z = '&z=21'
    url = "http://www.google.cn/maps/vt?lyrs=s@803&gl=cn&x="    # 1731111&y=836147&z=21"   
    for y in range(835900, 836302):        
        for x in range(1730000, 1731300):        
            img_url = url + str(x) + '&y=' + str(y) + z
            img = requests.get(img_url) 
            file = 'img/%s.jpg' %( str(x) + '****' + str(y))
            print(file)
            with open(file,'ab') as f: #存储图片，多媒体文件需要参数b（二进制文件）
                f.write(img.content) #多媒体存储content
            x += 1
            

def dj():
    for i in range(10, 50):
        print(i)            
            
    
def mergePicture(x):
    y = 835900
    img_list = []
    for y in range(835900, 836302):             
        imlist = []
        for x in range(1730000, 1731300):     
            file = 'img/%s.jpg' %( str(x) + '****' + str(y))
            print(file)
            img = Image.open(file)       
            imlist.append(img)
        jimg = image_joint(imlist, 'horizontal')        
        img_list.append(jimg)
    limg = image_joint(img_list, 'vertical')   
#    limg.show()
    limg.save('demo2.jpg', 'jpeg')
    
    
if __name__ == "__main__":
    x = 1730000
    y = 835900
    wirtePicture(x, y)
    mergePicture(x)
#    dj()
    
    

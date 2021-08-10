# -*- coding: utf-8 -*-
import  requests
import PIL.Image as Image

fileList = ['CARTclothes20200821_10.jpg', 'CARTclothes20200821_100.jpg', 'CARTclothes20200821_11.jpg', 'CARTclothes20200821_111.jpg', 'CARTclothes20200821_118.jpg', 'CARTclothes20200821_119.jpg', 'CARTclothes20200821_12.jpg', 'CARTclothes20200821_120.jpg', 'CARTclothes20200821_122.jpg', 'CARTclothes20200821_129.jpg', 'CARTclothes20200821_13.jpg', 'CARTclothes20200821_130.jpg', 'CARTclothes20200821_14.jpg', 'CARTclothes20200821_147.jpg', 'CARTclothes20200821_148.jpg', 'CARTclothes20200821_149.jpg', 'CARTclothes20200821_15.jpg', 'CARTclothes20200821_152.jpg', 'CARTclothes20200821_153.jpg', 'CARTclothes20200821_154.jpg', 'CARTclothes20200821_155.jpg', 'CARTclothes20200821_156.jpg', 'CARTclothes20200821_157.jpg', 'CARTclothes20200821_158.jpg', 'CARTclothes20200821_159.jpg', 'CARTclothes20200821_162.jpg', 'CARTclothes20200821_163.jpg', 'CARTclothes20200821_164.jpg', 'CARTclothes20200821_165.jpg', 'CARTclothes20200821_179.jpg', 'CARTclothes20200821_182.jpg', 'CARTclothes20200821_193.jpg', 'CARTclothes20200821_194.jpg', 'CARTclothes20200821_195.jpg', 'CARTclothes20200821_197.jpg', 'CARTclothes20200821_198.jpg', 'CARTclothes20200821_2.jpg', 'CARTclothes20200821_203.jpg', 'CARTclothes20200821_28.jpg', 'CARTclothes20200821_3.jpg', 'CARTclothes20200821_33.jpg', 'CARTclothes20200821_34.jpg', 'CARTclothes20200821_35.jpg', 'CARTclothes20200821_36.jpg', 'CARTclothes20200821_37.jpg', 'CARTclothes20200821_39.jpg', 'CARTclothes20200821_4.jpg', 'CARTclothes20200821_41.jpg', 'CARTclothes20200821_45.jpg', 'CARTclothes20200821_47.jpg', 'CARTclothes20200821_48.jpg', 'CARTclothes20200821_49.jpg', 'CARTclothes20200821_5.jpg', 'CARTclothes20200821_50.jpg', 'CARTclothes20200821_51.jpg', 'CARTclothes20200821_52.jpg', 'CARTclothes20200821_53.jpg', 'CARTclothes20200821_54.jpg', 'CARTclothes20200821_55.jpg', 'CARTclothes20200821_56.jpg', 'CARTclothes20200821_57.jpg', 'CARTclothes20200821_58.jpg', 'CARTclothes20200821_59.jpg', 'CARTclothes20200821_6.jpg', 'CARTclothes20200821_60.jpg', 'CARTclothes20200821_61.jpg', 'CARTclothes20200821_62.jpg', 'CARTclothes20200821_63.jpg', 'CARTclothes20200821_64.jpg', 'CARTclothes20200821_65.jpg', 'CARTclothes20200821_66.jpg', 'CARTclothes20200821_67.jpg', 'CARTclothes20200821_68.jpg', 'CARTclothes20200821_69.jpg', 'CARTclothes20200821_70.jpg', 'CARTclothes20200821_71.jpg', 'CARTclothes20200821_72.jpg', 'CARTclothes20200821_73.jpg', 'CARTclothes20200821_74.jpg', 'CARTclothes20200821_75.jpg', 'CARTclothes20200821_76.jpg', 'CARTclothes20200821_78.jpg', 'CARTclothes20200821_79.jpg', 'CARTclothes20200821_8.jpg', 'CARTclothes20200821_80.jpg', 'CARTclothes20200821_81.jpg', 'CARTclothes20200821_82.jpg', 'CARTclothes20200821_83.jpg', 'CARTclothes20200821_84.jpg', 'CARTclothes20200821_85.jpg', 'CARTclothes20200821_86.jpg', 'CARTclothes20200821_87.jpg', 'CARTclothes20200821_88.jpg', 'CARTclothes20200821_9.jpg', 'CARTclothes20200821_93.jpg', 'CARTclothes20200821_94.jpg', 'CARTclothes20200821_95.jpg', 'CARTclothes20200821_96.jpg', 'CARTclothes20200821_98.jpg', 'CARTclothes20200821_99.jpg']

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
            
def getFileFromWeb(webUrl):
    '''从网络上获取文件
        @param webUrl 网络地址
    '''
    for fileName in fileList:
        xmlName = fileName.split(".")[0] + ".xml"
        img_url = webUrl + fileName
        xml_url = webUrl + xmlName
        print(xml_url)
        img = requests.get(img_url) 
        imgSavePath = '/2020/clothes_person/%s' %(fileName)
        with open(imgSavePath,'ab') as f: #存储图片，多媒体文件需要参数b（二进制文件）
            f.write(img.content)  #多媒体存储content
        xml = requests.get(xml_url)
        xmlSavePath = '/2020/clothes_person/%s' % (xmlName)
        with open(xmlSavePath,'ab') as f: #存储图片，多媒体文件需要参数b（二进制文件）
            f.write(xml.content)  #多媒体存储content

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
    # x = 1730000
    # y = 835900
    # wirtePicture(x, y)
    # mergePicture(x)
#    dj()
    getFileFromWeb("https://minio.cvmart.net/test-image-pvc/0b1b99a6ad68a7b0110894aa18945afd/sample/fanguangyishibie/v2/")
    
    

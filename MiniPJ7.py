import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
import math
from PIL import Image #Thu vien PILLOW

#Main_program
filehinh = r'lena_color.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)
#Tạo 3 ảnh mới
hue = Image.new(imgPIL.mode, imgPIL.size)
saturation = Image.new(imgPIL.mode, imgPIL.size)
intensity = Image.new(imgPIL.mode, imgPIL.size)
hsi = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng
#Tạo ma trận 2 chiều để duyệt ảnh
for x in range(width):
    for y in range (height):
        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B = imgPIL.getpixel((x,y)) #getpixel -> B, G, R
        theta = math.acos(
                        (1/2) * 
                        ((R - G)+(R - B))/
                        (math.sqrt((R-G)*(R-G) + (R-B)*(G-B)))          
                        )
        if B <= G :
            Hu = theta
        else:
            Hu = (2*math.pi) - theta
        Hu = np.uint8(((Hu*180)/math.pi))
        Sa = (1 - 3 * (min(R, G, B) / (R+G+B)))
        Sa = np.uint8(Sa*255)
        In = np.uint8((R+G+B)/3)
        #Đặt giá trị pixel cho từng ảnh đã tạo
        hue.putpixel((x,y),(Hu, Hu, Hu))
        saturation.putpixel((x,y),(Sa, Sa, Sa))
        intensity.putpixel((x,y),(In, In, In))
        hsi.putpixel((x,y), (Hu, Sa, In))



#Chuyển ảnh từ PIL sang OpenCV  
Hue = np.array(hue)
Hue = cv2.cvtColor(Hue, cv2.COLOR_RGB2BGR) 
Sa = np.array(saturation)
Sa =cv2.cvtColor(Sa, cv2.COLOR_RGB2BGR) 
In = np.array(intensity)
In =cv2.cvtColor(In, cv2.COLOR_RGB2BGR) 
HSI = np.array(hsi)
HSI =cv2.cvtColor(HSI, cv2.COLOR_RGB2BGR) 
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh H', Hue)
cv2.imshow('Anh Sa', Sa)
cv2.imshow('Anh I', In)
cv2.imshow('Anh HSI', HSI)
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

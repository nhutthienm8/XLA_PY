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
#Tạo 1 ảnh mới
Shrpned_img = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng

for x in range(1,width-1):
    for y in range (1,height-1):
        #Lấy giá trị điểm ảnh tại các vị trí 
        R,G,B = imgPIL.getpixel((x,y))
        R1,G1,B1 = imgPIL.getpixel((x+1,y))
        R2,G2,B2 = imgPIL.getpixel((x-1,y))
        R3,G3,B3 = imgPIL.getpixel((x,y+1))
        R4,G4,B4 = imgPIL.getpixel((x,y-1)) 
        g_R = 5*R - R1 - R2 - R3 - R4
        g_G = 5*G - G1 - G2 - G3 - G4 
        g_B = 5*B - B1 - B2 - B3 - B4
        Shrpned_img.putpixel((x,y),(g_R,g_G,g_B))     
#Chuyển ảnh từ PIL sang OpenCV
S_img = np.array(Shrpned_img)
S_img = cv2.cvtColor(S_img, cv2.COLOR_RGB2BGR)        
        

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh lam sac net', S_img)

#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

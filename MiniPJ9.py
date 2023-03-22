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
X = Image.new(imgPIL.mode, imgPIL.size)
Y = Image.new(imgPIL.mode, imgPIL.size)
Z = Image.new(imgPIL.mode, imgPIL.size)
XYZ = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng
#Tạo ma trận 2 chiều để duyệt ảnh
for x in range(width):
    for y in range (height):
        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B = imgPIL.getpixel((x,y)) 
        Xv = np.uint8(0.4124564*R + 0.3575761*G + 0.1804375*B)
        Yv = np.uint8(0.2126729*R + 0.7151522*G + 0.0721750*B)
        Zv = np.uint8(0.0193339*R + 0.1191920*G + 0.9503041*B)
        X.putpixel((x,y), (Xv,Xv,Xv))
        Y.putpixel((x,y), (Yv,Yv,Yv))
        Z.putpixel((x,y), (Zv,Zv,Zv))
        XYZ.putpixel((x,y), (Xv,Yv,Zv))

#Chuyển ảnh từ PIL sang OpenCV  
X_cv = np.array(X)
X_cv = cv2.cvtColor(X_cv, cv2.COLOR_RGB2BGR) 
Y_cv = np.array(Y)
Y_cv =cv2.cvtColor(Y_cv, cv2.COLOR_RGB2BGR) 
Z_cv = np.array(Z)
Z_cv =cv2.cvtColor(Z_cv, cv2.COLOR_RGB2BGR) 
XYZ_cv = np.array(XYZ)
XYZ_cv =cv2.cvtColor(XYZ_cv, cv2.COLOR_RGB2BGR) 
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh X', X_cv)
cv2.imshow('Anh Y', Y_cv)
cv2.imshow('Anh Z', Z_cv)
cv2.imshow('Anh XYZ', XYZ_cv)
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

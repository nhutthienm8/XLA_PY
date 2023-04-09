import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
import math
from PIL import Image #Thu vien PILLOW
def smoothed (imgPIL,A):
    iA = int (A/2)
    K = A*A
    SMTH_IMG = Image.new(imgPIL.mode, imgPIL.size)
    for x in range(iA,width-iA):
        for y in range (iA,height-iA):
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x-int(A/2),x+1+int(A/2)):
                for j in range(y-int(A/2),y+1+int(A/2)):
                    R,G,B = imgPIL.getpixel((i,j))
                    Rs += R
                    Gs += G
                    Bs += B
            Rs = np.uint8(Rs * 1/K)
            Gs = np.uint8(Gs * 1/K)
            Bs = np.uint8(Bs * 1/K)
            SMTH_IMG.putpixel((x,y), (Rs,Gs,Bs))
    return SMTH_IMG
#Main_program
filehinh = r'lena_color.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)
#Tạo 1 ảnh mới
SMTH_IMG_3X3 = Image.new(imgPIL.mode, imgPIL.size)
SMTH_IMG_5X5 = Image.new(imgPIL.mode, imgPIL.size)
SMTH_IMG_7X7 = Image.new(imgPIL.mode, imgPIL.size)
SMTH_IMG_9X9 = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng
#Làm mượt ảnh 3x3
SMTH_IMG_3X3 = smoothed(imgPIL,3)
#Làm mượt ảnh 5x5
SMTH_IMG_5X5 = smoothed(imgPIL,5)
#Làm mượt ảnh 7x7
SMTH_IMG_7X7 = smoothed(imgPIL,7)
#Làm mượt ảnh 9x9
SMTH_IMG_9X9 = smoothed(imgPIL,9)

#Chuyển ảnh từ PIL sang OpenCV
SMTH_IMG_3x3 = np.array(SMTH_IMG_3X3)
SMTH_IMG_3x3 = cv2.cvtColor(SMTH_IMG_3x3, cv2.COLOR_RGB2BGR)
SMTH_IMG_5x5 = np.array(SMTH_IMG_5X5)
SMTH_IMG_5x5 = cv2.cvtColor(SMTH_IMG_5x5, cv2.COLOR_RGB2BGR)   
SMTH_IMG_7x7 = np.array(SMTH_IMG_7X7)
SMTH_IMG_7x7 = cv2.cvtColor(SMTH_IMG_7x7, cv2.COLOR_RGB2BGR)   
SMTH_IMG_9x9 = np.array(SMTH_IMG_9X9)
SMTH_IMG_9x9 = cv2.cvtColor(SMTH_IMG_9x9, cv2.COLOR_RGB2BGR)            
        

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh lam muot 3x3', SMTH_IMG_3x3)
cv2.imshow('Anh la muot 5x5', SMTH_IMG_5x5)
cv2.imshow('Anh lam muot 7x7', SMTH_IMG_7x7)
cv2.imshow('Anh lam muot 9x9', SMTH_IMG_9x9)
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

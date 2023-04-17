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
Edge_img = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng

#Nhập ngưỡng
print("Nhập ngưỡng")
D0 = float(input())
#Mảng Sobel Sx
Sx = np.array([[-1,-2,-1],
              [0,0,0],
              [1,2,1]], dtype=int)
#Mảng Sobel Sy
Sy = np.array([[-1,0,1],
              [-2,0,2],
              [-1,0,1]], dtype=int)
#Set giá trị cho từng pixel
for x in range(1,width-1):
    for y in range (1,height-1):
        #Tính các gx, gy
        gxR = 0
        gxG = 0
        gxB = 0
        gyR = 0
        gyG = 0
        gyB = 0
        for i in range (x-1,x+2):
            for j in range (y-1,y+2):
                R,G,B = imgPIL.getpixel((i,j))
                gxR += R * Sx[i-x+1,j-y+1]
                gxG += G * Sx[i-x+1,j-y+1]
                gxB += B * Sx[i-x+1,j-y+1]

                gyR += R * Sy[i-x+1,j-y+1]
                gyG += G * Sy[i-x+1,j-y+1]
                gyB += B * Sy[i-x+1,j-y+1]

                
        #Tính gxx gyy gxy
        gxx = math.pow(gxR,2) + math.pow(gxG,2) + math.pow(gxB,2)
        gyy = gyR * gyR + gyG * gyG + gyB * gyB
        gxy = gxR * gyR + gxG * gyG + gxB * gyB
        #Tính theta dùng atan2 để tránh gxx-gyy=0
        theta = math.atan2((2 * gxy) , (gxx-gyy))* (1 / 2)
        #Tính F
        F = math.sqrt(((gxx+gyy)+(gxx-gyy)*math.cos(2*theta)+2*gxy*math.sin(2*theta))/2)
        #So sánh với ngưỡng (>= ngưỡng là đường biên)
        if F <= D0 :
            Edge_img.putpixel((x,y),(0,0,0))
        else :
            Edge_img.putpixel((x,y),(255,255,255))
                
#Chuyển ảnh từ PIL sang OpenCV
edge_img = np.array(Edge_img)
edge_img = cv2.cvtColor(edge_img, cv2.COLOR_RGB2BGR)           
        

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh RGB', img)
cv2.imshow('Anh duong bien', edge_img)

#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
import math
from PIL import Image #Thu vien PILLOW

def GrayImg (imgpil):
    #Tạo ảnh có cùng kích thước để chuyển đổi Grayscale
    average = Image.new(imgPIL.mode, imgPIL.size)
    #Tạo ma trận 2 chiều để duyệt ảnh
    for x in range(width):
        for y in range (height):
            #Lấy giá trị điểm ảnh tại vị trí (x,y)
            R, G, B = imgPIL.getpixel((x,y))

            #Lấy giá trị màu xám dùng AVG
            gray = np.uint8((R+G+B)/3)   #np.uint8 : ép kiểu về 8 bit

            #Gán giá trị gray cho từng pixel trong ảnh mới
            average.putpixel((x,y), (gray,gray,gray))
    return average
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
#Tạo ảnh mức xám
average_Img = GrayImg(imgPIL)
#Nhập ngưỡng
print("Nhập ngưỡng")
D0 = int(input())

#Set giá trị cho từng pixel
for x in range(1,width-1):
    for y in range (1,height-1):
        arr = []
        for i in range (x-1, x+2):
            for j in range (y-1, y+2):
                R,G,B = average_Img.getpixel((i,j))
                arr.append(R)
        #Tính gx
        gx = (arr[6] + 2*arr[7] + arr[8]) - (arr[0] + 2*arr[1] + arr[2])
        #Tính gy
        gy = (arr[2] + 2*arr[5] + arr[8]) - (arr[0] + 2*arr[3] + arr[6])
        #Tính M
        M = np.abs(gx)+np.abs(gy)
        #So sánh với ngưỡng (>= ngưỡng là đường biên)
        if M < D0 :
            Edge_img.putpixel((x,y),(0,0,0))
        else :
            Edge_img.putpixel((x,y),(255,255,255))
                
#Chuyển ảnh từ PIL sang OpenCV
gray_img = np.array(average_Img)
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_RGB2BGR)
edge_img = np.array(Edge_img)
edge_img = cv2.cvtColor(edge_img, cv2.COLOR_RGB2BGR)           
        

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh muc xam', gray_img)
cv2.imshow('Anh duong bien', edge_img)

#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

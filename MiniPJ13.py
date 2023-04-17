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
Seg_img = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng
#Lấy vùng cần xét
print("Nhap diem A1 (x1,y1)")
x1 = int(input())
y1 = int(input()) 
print("Nhap diem A2 (x2,y2)")
x2 = int(input())
y2 = int(input())
#Nhập ngưỡng
print("Nhập ngưỡng")
D0 = int(input())

#Giá trị RGB của a
aR = 0
aG = 0
aB = 0
for x in range(x1,x2):
    for y in range (y1,y2):
        #Lấy giá trị điểm ảnh tại các vị trí
        R,G,B = imgPIL.getpixel((x,y))
        aR += R
        aG += G
        aB += B       
aR /= np.abs(x2-x1)*np.abs(y2-y1) 
aG /= np.abs(x2-x1)*np.abs(y2-y1) 
aB /= np.abs(x2-x1)*np.abs(y2-y1) 
#Set giá trị cho từng pixel
for x in range(0,width):
    for y in range (0,height):
        #Lấy giá trị điểm ảnh tại các vị trí 
        R,G,B = imgPIL.getpixel((x,y))
        D = math.sqrt(math.pow(R-aR,2)+math.pow(G-aG,2)+math.pow(B-aB,2))
        if D <= D0:
            Seg_img.putpixel((x,y),(255,255,255)) 
        else:
            Seg_img.putpixel((x,y),(R,G,B))
             
#Chuyển ảnh từ PIL sang OpenCV
Seg_IMG = np.array(Seg_img)
Seg_IMG = cv2.cvtColor(Seg_IMG, cv2.COLOR_RGB2BGR)        
        

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh da xoa phong', Seg_IMG)

#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

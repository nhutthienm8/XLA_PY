import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
from PIL import Image #Thu vien PILLOW

#Main_program
filehinh = r'lena_color.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)
#Tạo 3 ảnh mới
cyan = Image.new(imgPIL.mode, imgPIL.size)
magenta = Image.new(imgPIL.mode, imgPIL.size)
yellow = Image.new(imgPIL.mode, imgPIL.size)
black = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước
width = imgPIL.size[0] #chiều dài
height = imgPIL.size[1] #chiều rộng
#Tạo ma trận 2 chiều để duyệt ảnh
for x in range(width):
    for y in range (height):
        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B = imgPIL.getpixel((x,y)) #getpixel -> B, R, G
        #Đặt giá trị pixel cho từng ảnh đã tạo
        cyan.putpixel((x,y),(0,G,B))
        magenta.putpixel((x,y),(R,0,B))
        yellow.putpixel((x,y),(R,G,0))
        K = np.uint8((R+G+B)/3)
        black.putpixel((x,y),(K,K,K))


#Chuyển ảnh từ PIL sang OpenCV 
Cyan = np.array(cyan)
Cyan=cv2.cvtColor(Cyan, cv2.COLOR_RGB2BGR) 
Magenta = np.array(magenta)
Magenta=cv2.cvtColor(Magenta, cv2.COLOR_RGB2BGR) 
Yellow = np.array(yellow)
Yellow=cv2.cvtColor(Yellow, cv2.COLOR_RGB2BGR) 
Black = np.array(black)
Black=cv2.cvtColor(Black, cv2.COLOR_RGB2BGR) 
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh cyan', Cyan)
cv2.imshow('Anh magenta', Magenta)
cv2.imshow('Anh yellow', Yellow)
cv2.imshow('Anh black', Black)
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

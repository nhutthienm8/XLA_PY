import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học 
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread('Lena.PNG', cv2.IMREAD_COLOR)
#Lấy kích thước của ảnh 
height = len(img[0])
width = len(img[1])
#Khai báo 3 biến để chứa hình 3 kênh RGB
red = np.zeros((width, height, 3), np.uint8) #số 3 là ba kênh RGB, mỗi kênh 8bit
green = np.zeros((width, height, 3), np.uint8)
blue = np.zeros((width, height, 3), np.uint8)

#Set 3 kênh cho giá trị zero
red[:]= [0,0,0]
green[:]= [0,0,0]
blue[:]= [0,0,0]

for x in range(height):
    for y in range (width):
        R = img[x, y, 2]
        G = img[x,y,1]
        B = img[x,y,0]

    #thiết lập màu cho các kênh
        red[x,y,2] = R
        green[x,y,1] = G
        blue[x,y,0] = B

#Hiển thị hình dùng thư viện openCV
cv2.imshow('Anh_nude_1.jpg', img)
cv2.imshow('Kenh_RED', red)
cv2.imshow('Kenh_GREEN', green)
cv2.imshow('Kenh_BLUE', blue)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát
cv2.destroyAllWindows()



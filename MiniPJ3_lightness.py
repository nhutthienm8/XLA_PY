import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
from PIL import Image #Thu vien PILLOW
filehinh = r'lena_color.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)

#Tạo ảnh có cùng kích thước để chuyển đổi Grayscale
average = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước 
width = average.size[0] #chiều dài
height = average.size[1] #chiều rộng
#Tạo ma trận 2 chiều để duyệt ảnh
for x in range(width):
    for y in range (height):
        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x,y))

        #Lấy giá trị MIN, MAX
        MIN = min(R, G, B)
        MAX = max(R, G, B)
        gray = np.uint8((MAX + MIN)/2)      #np.uint8 : ép kiểu về 8 bit
        average.putpixel((x, y), (gray, gray, gray))

#Chuyển ảnh từ PIL sang OpenCV 
anhmucxam = np.array(average)

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh muc xam', anhmucxam)

#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()
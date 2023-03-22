import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
from PIL import Image #Thu vien PILLOW
import matplotlib.pyplot as plt #Thư viện vẽ biểu đồ

#Hàm chuyển đổi ảnh mức xám
def GrayImage (imgPIL):
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

            #Lấy giá trị màu xám dùng AVG
            gray = np.uint8((R+G+B)/3)   #np.uint8 : ép kiểu về 8 bit
            average.putpixel((x,y), (gray, gray, gray))
    return average


def Histogram (HinhxamPIL):
    #Khai báo mảng chứa giá trị của mỗi pixel mức xám trong ảnh
    his = np.zeros(256)

    #Kích thước của ảnh
    w = HinhxamPIL.size[0]
    h = HinhxamPIL.size[1]
    for x in range (w):
        for y in range (h):
            #Lấy giá trị xám tại điểm (x, y)
            gR, gG, gB = HinhxamPIL.getpixel((x,y))

            his[gR] += 1
    return his

#Vẽ biểu đồ Histogram
def drawHis (his):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh xám', figsize=(((w,h))), dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0,256,256)
    plt.plot(trucX, his, color = 'orange')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị RGB')
    plt.ylabel('Số điểm cùng giá trị R/G/B')
    plt.show()


#Main_program
filehinh = r'bird_small.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien PIL
imgPIL = Image.open(filehinh)

HinhxamPIL = GrayImage(imgPIL)
#Chuyển ảnh từ PIL sang OpenCV 
anhmucxam = np.array(HinhxamPIL)
#Hiển thị ảnh dùng thư viện OpenCV 
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh muc xam', anhmucxam)
drawHis(Histogram(HinhxamPIL))
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

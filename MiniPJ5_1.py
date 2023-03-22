import cv2 #thư viện xử lý ảnh
import numpy as np #thư viện toán học
from PIL import Image #Thu vien PILLOW
import matplotlib.pyplot as plt #Thư viện vẽ biểu đồ
def Histogram (HinhxamPIL):
    #Khai báo mảng chứa giá trị của mỗi pixel mức xám trong ảnh
    his = np.zeros((3, 256))
    #Dùng mảng 2 chiều 3 dòng 256 cột để lưu giá trị Pixel của 3 kênh RGB
    #1 - R
    #2 - G
    #3 - B
    #Kích thước của ảnh
    w = HinhxamPIL.size[0]
    h = HinhxamPIL.size[1]
    for x in range (w):
        for y in range (h):
            #Lấy giá trị xám tại điểm (x, y)
            gR, gG, gB = HinhxamPIL.getpixel((x,y))

            his[0, gR] += 1
            his[1, gG] += 1
            his[2, gB] += 1
    return his

#Vẽ biểu đồ Histogram
def drawHis (his):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh RGB', figsize=(((w,h))), dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0,256,256)
    plt.plot(trucX, his[0], color = 'red')
    plt.plot(trucX, his[1], color = 'green')
    plt.plot(trucX, his[2], color = 'blue')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()


#Main_program
filehinh = r'bird_small.jpg'
#Đọc ảnh màu dùng thư viện openCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
drawHis(Histogram(imgPIL))
#Bấm phím bất kỳ để out 
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ 
cv2.destroyAllWindows()

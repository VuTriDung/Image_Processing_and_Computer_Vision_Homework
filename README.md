# 📸 Image Processing and Computer Vision - Course Project

Chào mừng đến với kho lưu trữ đồ án môn Xử lý ảnh và Thị giác máy tính (Image Processing and Computer Vision). Dự án này là tập hợp các bài thực hành các tuần, ứng dụng ngôn ngữ lập trình Python và thư viện máy học/xử lý ảnh để giải quyết các bài toán thực tế.

## 🌟 Tổng quan dự án

Mục tiêu của dự án không chỉ dừng lại ở việc áp dụng các bộ lọc (filters) có sẵn, mà còn tập trung vào việc **xây dựng các hệ thống đánh giá tự động (Auto-Detectors)**. Thay vì hard-code các thông số, hệ thống sẽ tự động phân tích dữ liệu thống kê của bức ảnh (Mean, Standard Deviation, Histogram, Outlier Ratio) để đưa ra quyết định xử lý tối ưu nhất.

### 🛠️ Công nghệ & Thư viện sử dụng
* **Python 3.x:** Ngôn ngữ lập trình lõi.
* **OpenCV (`cv2`):** Thư viện cốt lõi dùng để đọc, ghi, chuyển đổi không gian màu và áp dụng các thuật toán xử lý không gian.
* **NumPy (`numpy`):** Xử lý ma trận điểm ảnh tốc độ cao, tính toán thống kê và áp dụng các công thức toán học (như Gamma Correction).
* **Matplotlib (`matplotlib`):** Trực quan hóa dữ liệu, vẽ biểu đồ Histogram và tạo các Dashboard báo cáo so sánh Before/After.
* **SciPy (`scipy`):** Cung cấp hàm `scipy.signal.convolve` để mô phỏng và đo lường độ phức tạp của thuật toán tích chập (Convolution Benchmark).

## 📂 Cấu trúc thư mục chi tiết
```bash
    📦 Image_Processing_and_Computer_Vision_Homework
     ┣ 📂 Week1
     ┃ ┣ 📂 images
     ┃ ┣ 📂 ... (các folder output bài tập tuần 1)
     ┃ ┣ 📜 README.md
     ┃ ┗ 📜 ... (các file code tuần 1)
     ┣ 📂 Week2+3
     ┃ ┣ 📂 images
     ┃ ┣ 📂 ... (các folder output bài tập tuần 1)
     ┃ ┣ 📜 README.md
     ┃ ┗ 📜 ... (các file code tuần 1)
     ┣ 📂 ... (Các folder bài tập các tuần sau sẽ cập nhật thêm)
     ┣ 📜 requirements.txt
     ┗ 📜 README.md
```
## ⚙️ Hướng dẫn cài đặt & Khởi chạy (Windows)

Để tránh xung đột thư viện, khuyến nghị dùng Virtual Environment.

**Bước 1: Khởi tạo môi trường ảo**
```bash
    python -m venv myenv
```

**Bước 2: Kích hoạt môi trường ảo**
```bash
    myenv\Scripts\activate
```

(Thành công khi xuất hiện tiền tố (myenv))

**Bước 3: Cài dependencies**
```bash
    pip install -r requirements.txt
```

**Bước 4: Chạy chương trình**
```bash
    cd Week2+3
    python adaptive_brightness.py
```
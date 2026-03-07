# Bài tập Xử lý ảnh và Thị giác máy tính - Tuần 1

Mục tiêu của dự án này là thực hành Python, OpenCV và NumPy để làm việc với ảnh ở mức pixel (tách kênh màu, thay đổi độ sáng/tương phản, thay đổi độ phân giải và tự tạo ảnh bằng toán học).

## 📁 Cấu trúc thư mục

- `channels_gray.py`: Bài 1 - Tách kênh màu (R, G, B) và chuyển đổi Grayscale.
- `intensity_ops.py`: Bài 2 - Chỉnh sửa ảnh cơ bản (sáng, tối, tương phản, threshold).
- `resampling.py`: Bài 3 - Giảm độ phân giải ảnh bằng Slicing ma trận.
- `synthetic_images.py`: Bài 4 - Tự tạo ảnh (Gradient, Checkerboard, Circle) bằng code.
- `images/`: Thư mục chứa ảnh gốc đầu vào.
- `output_bai.../`: Các thư mục tự động sinh ra để chứa ảnh kết quả.

## 🛠️ Hướng dẫn cài đặt và chạy Code
Dự án này sử dụng môi trường ảo (Virtual Environment) để quản lý các thư viện. Vui lòng làm theo các bước sau:

### Bước 1: Tạo môi trường ảo (venv)
Mở Terminal tại thư mục gốc của dự án và gõ lệnh:
```bash
python -m venv myenv
```

### Bước 2: Kích hoạt môi trường ảo
Bạn bắt buộc phải kích hoạt môi trường trước khi chạy code hoặc cài đặt thư viện.
- Trên Window:
```bash
.\myenv\Scripts\activate
```
- Trên MacOS/Linux:
```bash
source myenv/bin/activate
```

(Dấu hiệu thành công: Có chữ (myenv) xuất hiện màu xanh ở đầu dòng lệnh)

### Bước 3: Cài đặt thư viện
Đảm bảo môi trường đã được kích hoạt, tiến hành cài đặt OpenCV và NumPy bằng lệnh:
```bash
pip install opencv-python numpy
```

Khi làm việc với ảnh thì nên hiển thị ảnh ra màn hình để xem kết quả. Nên cài thêm matplotlib bằng lệnh:
```bash
pip install matplotlib
```

### Bước 4: Chạy thử kiểm tra
Bạn có thể mở từng file lên và bấm nút Run trên VS Code, hoặc chạy bằng lệnh trong terminal:
```bash
python channels_gray.py
```

---
**Hoặc cài đặt toàn bộ thư viện tự động từ file (Khuyên dùng):**
```bash
pip install -r requirements.txt
```
Vì người push git này đã sử dụng file requirements.txt để người khác clone về chỉ cần dùng lệnh ở trên đảm bảo đúng phiên bản và đúng cầu hình để Run cho mượt và đúng. Dòng lệnh dưới đây là dòng lệnh dành cho người push lên:
```bash
pip freeze > requirements.txt
```


# 🎨 Week 1: Digital Image Fundamentals & Color Spaces

Thư mục này chứa các bài tập nhập môn, thiết lập nền tảng vững chắc về cách máy tính biểu diễn và hiểu một bức ảnh kỹ thuật số.

## 🎯 Trọng tâm lý thuyết
Một bức ảnh kỹ thuật số bản chất là một ma trận 2D (đối với ảnh xám) hoặc 3D (đối với ảnh màu) chứa các giá trị pixel (từ 0 đến 255). 

1. **Hệ màu mặc định của OpenCV (BGR):** Khác với chuẩn RGB thông thường, OpenCV nạp ảnh vào bộ nhớ theo thứ tự Blue - Green - Red. Việc hiểu rõ thứ tự này rất quan trọng khi thực hiện các thao tác tách/gộp kênh.
2. **Ảnh đa cấp xám (Grayscale):** Chuyển đổi một bức ảnh màu sang thang độ xám không đơn thuần là lấy trung bình cộng 3 kênh, mà thường áp dụng công thức có trọng số dựa trên độ nhạy của mắt người:
   $$Y = 0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B$$

## 🛠️ Các thao tác thực hành chính
* **Đọc và Ghi ảnh:** Sử dụng `cv2.imread()` để nạp ma trận ảnh từ ổ cứng và `cv2.imwrite()` để xuất ma trận ra thành file ảnh chuẩn (JPG/PNG).
* **Tách kênh màu (Splitting):** Dùng `cv2.split()` để tách bức ảnh thành 3 ma trận độc lập, giúp phân tích sự phân bố của từng phổ màu.
* **Gộp kênh màu (Merging):** Dùng `cv2.merge()` để tái tổ hợp các kênh màu sau khi đã qua chỉnh sửa, hoặc dùng để trực quan hóa một kênh màu duy nhất trong không gian 3D bằng cách triệt tiêu (set bằng 0) các kênh còn lại.

## 🚀 Hướng dẫn chạy
* Nạp các bức ảnh cần test vào thư mục chứa code.
* Mở terminal và chạy các file `.py` tương ứng. Giao diện GUI của `matplotlib` hoặc `cv2.imshow` sẽ hiển thị kết quả phân tách màu.
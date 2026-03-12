import cv2
import numpy as np
import os  # Thêm thư viện os để tương tác với hệ thống file/thư mục

# --- TẠO THƯ MỤC CHỨA KẾT QUẢ ---
output_dir = "output_bai1"
# Lệnh này sẽ tạo folder 'output_bai1'. 
# exist_ok=True nghĩa là nếu folder đã có sẵn thì nó bỏ qua, không báo lỗi.
os.makedirs(output_dir, exist_ok=True) 

# --- 1. ĐỌC ẢNH VÀ TÁCH KÊNH MÀU ---
img = cv2.imread('images/pic_week1.jpg')

if img is None:
    print("Lỗi: Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn.")
    exit()

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

# Lưu từng kênh ra file vào trong thư mục output_bai1
# os.path.join sẽ tự động nối tên thư mục và tên file lại với nhau cho chuẩn xác
cv2.imwrite(os.path.join(output_dir, 'blue.png'), B)
cv2.imwrite(os.path.join(output_dir, 'green.png'), G)
cv2.imwrite(os.path.join(output_dir, 'red.png'), R)

# --- 2. CHUYỂN ĐỔI RGB -> GRAYSCALE ---
B_f = B.astype(np.float32)
G_f = G.astype(np.float32)
R_f = R.astype(np.float32)

# Option 1: Tính trung bình cộng (R + G + B) / 3 (Làm thêm để so sánh)
gray_avg = (R_f + G_f + B_f) / 3
gray_option1 = np.clip(gray_avg, 0, 255).astype(np.uint8)
cv2.imwrite(os.path.join(output_dir, 'gray_option1.png'), gray_option1)

# Option 2: Tính theo trọng số Luminosity 0.299R + 0.587G + 0.114B (Lưu đúng tên đề yêu cầu)
gray_lum = 0.299 * R_f + 0.587 * G_f + 0.114 * B_f
gray_manual = np.clip(gray_lum, 0, 255).astype(np.uint8)
cv2.imwrite(os.path.join(output_dir, 'gray_manual.png'), gray_manual)

# --- 3. SO SÁNH VÀ IN KẾT QUẢ ---
print("--- THÔNG SỐ SHAPE ---")
print(f"Ảnh màu gốc : {img.shape}")
print(f"Kênh Blue   : {B.shape}")
print(f"Kênh Green  : {G.shape}")
print(f"Kênh Red    : {R.shape}")
print(f"Ảnh Gray    : {gray_manual.shape}")
print(f"-> Đã lưu thành công các file ảnh vào thư mục: {output_dir}/")
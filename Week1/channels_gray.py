import cv2
import numpy as np
import os

# --- TỰ ĐỘNG TÌM ĐƯỜNG DẪN CHUẨN ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_bai1")
os.makedirs(output_dir, exist_ok=True)

img_path = os.path.join(current_dir, "images", "pic_week1.jpg")

# --- 1. ĐỌC ẢNH VÀ TÁCH KÊNH MÀU ---
img = cv2.imread(img_path)

if img is None:
    print(f"Lỗi: Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn: {img_path}")
    exit()

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

cv2.imwrite(os.path.join(output_dir, 'blue.png'), B)
cv2.imwrite(os.path.join(output_dir, 'green.png'), G)
cv2.imwrite(os.path.join(output_dir, 'red.png'), R)

# --- 2. CHUYỂN ĐỔI RGB -> GRAYSCALE ---
B_f = B.astype(np.float32)
G_f = G.astype(np.float32)
R_f = R.astype(np.float32)

# Option 1: Trung bình cộng
gray_avg = (R_f + G_f + B_f) / 3
gray_option1 = np.clip(gray_avg, 0, 255).astype(np.uint8)
cv2.imwrite(os.path.join(output_dir, 'gray_option1.png'), gray_option1)

# Option 2: Trọng số Luminosity
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
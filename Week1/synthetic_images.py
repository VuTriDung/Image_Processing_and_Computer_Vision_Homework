import cv2
import numpy as np
import os

# --- TỰ ĐỘNG TÌM ĐƯỜNG DẪN CHUẨN ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_bai4")
os.makedirs(output_dir, exist_ok=True)

# --- 1. TẠO ẢNH SYNTHETIC (256x256) BẰNG TOÁN HỌC ---
row = np.arange(256, dtype=np.uint8)
gradient = np.tile(row, (256, 1))

checkerboard = np.zeros((256, 256), dtype=np.uint8)
square_size = 32
for i in range(256):
    for j in range(256):
        if (i // square_size + j // square_size) % 2 == 0:
            checkerboard[i, j] = 255

y, x = np.indices((256, 256))
circle = np.where((x - 128)**2 + (y - 128)**2 <= 60**2, 255, 0).astype(np.uint8)

# --- LƯU ẢNH GRAYSCALE VÀ KIỂM TRA ---
cv2.imwrite(os.path.join(output_dir, 'gradient.png'), gradient)
cv2.imwrite(os.path.join(output_dir, 'checkerboard.png'), checkerboard)
cv2.imwrite(os.path.join(output_dir, 'circle.png'), circle)

print("--- KIỂM TRA ĐỊNH DẠNG VÀ KÍCH THƯỚC MA TRẬN ---")
print(f"Gradient     - Shape: {gradient.shape}, Dtype: {gradient.dtype}")
print(f"Checkerboard - Shape: {checkerboard.shape}, Dtype: {checkerboard.dtype}")
print(f"Circle       - Shape: {circle.shape}, Dtype: {circle.dtype}")

# --- 2. (TÙY CHỌN) CHUYỂN SANG RGB BẰNG CÁCH GHÉP KÊNH ---
rgb_synthetic = cv2.merge([circle, checkerboard, gradient])
cv2.imwrite(os.path.join(output_dir, 'rgb_synthetic.png'), rgb_synthetic)

print("\n--- KẾT QUẢ GHÉP KÊNH RGB ---")
print(f"RGB Ảnh ghép - Shape: {rgb_synthetic.shape}, Dtype: {rgb_synthetic.dtype}")
print(f"-> Đã lưu toàn bộ ảnh tạo bằng code vào thư mục: {output_dir}/")
import cv2
import numpy as np
import os

# --- TẠO THƯ MỤC CHỨA KẾT QUẢ ---
output_dir = "output_bai4"
os.makedirs(output_dir, exist_ok=True)

# --- 1. TẠO ẢNH SYNTHETIC (256x256) BẰNG TOÁN HỌC ---

# Ảnh 1: Gradient ngang (Từ đen 0 sang trắng 255)
# np.arange(256) tạo ra 1 hàng có các số từ 0 đến 255.
# np.tile copy hàng đó thành 256 hàng chồng lên nhau để tạo thành ma trận 256x256.
row = np.arange(256, dtype=np.uint8)
gradient = np.tile(row, (256, 1))

# Ảnh 2: Checkerboard (Bàn cờ caro)
# Tạo một nền đen 256x256 trước
checkerboard = np.zeros((256, 256), dtype=np.uint8)
square_size = 32 # Kích thước mỗi ô vuông là 32x32 pixel

# Dùng vòng lặp duyệt qua từng pixel để tô màu dựa trên tọa độ chẵn/lẻ
for i in range(256):
    for j in range(256):
        # Thuật toán tô ô bàn cờ kinh điển
        if (i // square_size + j // square_size) % 2 == 0:
            checkerboard[i, j] = 255

# Ảnh 3: Vòng tròn trắng trên nền đen
# Tạo 2 ma trận x, y chứa tọa độ của từng pixel
y, x = np.indices((256, 256))

# Áp dụng phương trình đường tròn tâm (128, 128), bán kính R=60. 
# Nếu điểm nào thỏa mãn phương trình thì cho bằng 255 (trắng), ngược lại 0 (đen).
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
# Chúng ta sẽ chơi lớn: Trộn 3 bức ảnh đen trắng vừa tạo thành 1 bức ảnh màu duy nhất!
# Kênh Blue = Hình tròn, Kênh Green = Bàn cờ, Kênh Red = Gradient
rgb_synthetic = cv2.merge([circle, checkerboard, gradient])

cv2.imwrite(os.path.join(output_dir, 'rgb_synthetic.png'), rgb_synthetic)

print("\n--- KẾT QUẢ GHÉP KÊNH RGB ---")
print(f"RGB Ảnh ghép - Shape: {rgb_synthetic.shape}, Dtype: {rgb_synthetic.dtype}")
print(f"-> Đã lưu toàn bộ ảnh tạo bằng code vào thư mục: {output_dir}/")
import cv2
import numpy as np
import os

# --- TỰ ĐỘNG TÌM ĐƯỜNG DẪN CHUẨN ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_bai2")
os.makedirs(output_dir, exist_ok=True)

img_path = os.path.join(current_dir, "images", "pic_week1.jpg")

# --- HÀM TỰ CÀI ĐẶT ĐỂ ĐẢM BẢO GIÁ TRỊ [0, 255] ---
def clip_uint8(arr):
    return np.clip(arr, 0, 255).astype(np.uint8)

# --- 1. ĐỌC ẢNH VÀ CHỈNH SÁNG / TỐI / TƯƠNG PHẢN ---
gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print(f"Lỗi: Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn: {img_path}")
    exit()

gray_float = gray.astype(np.float32)

gray_dark = clip_uint8(gray_float - 50)
gray_bright = clip_uint8(gray_float + 50)
gray_contrast = clip_uint8(gray_float * 1.5)

# --- 2. TỰ CÀI ĐẶT THRESHOLD NHỊ PHÂN ---
T = 128
binary = np.where(gray >= T, 255, 0).astype(np.uint8)

# --- LƯU ẢNH RA THƯ MỤC ---
cv2.imwrite(os.path.join(output_dir, 'gray_original.png'), gray)
cv2.imwrite(os.path.join(output_dir, 'gray_dark.png'), gray_dark)
cv2.imwrite(os.path.join(output_dir, 'gray_bright.png'), gray_bright)
cv2.imwrite(os.path.join(output_dir, 'gray_contrast.png'), gray_contrast)
cv2.imwrite(os.path.join(output_dir, 'binary_threshold.png'), binary)

# --- 3. IN SO SÁNH GIÁ TRỊ PIXEL ---
row, col = 100, 100
print(f"--- SO SÁNH PIXEL TẠI TỌA ĐỘ [{row}, {col}] ---")
print(f"Giá trị ảnh gốc        : {gray[row, col]}")
print(f"Giá trị ảnh tối hơn    : {gray_dark[row, col]}")
print(f"Giá trị ảnh sáng hơn   : {gray_bright[row, col]}")
print(f"Giá trị ảnh tương phản : {gray_contrast[row, col]}")
print(f"Giá trị ảnh nhị phân   : {binary[row, col]}")
print(f"-> Đã lưu các ảnh thành công vào thư mục: {output_dir}/")
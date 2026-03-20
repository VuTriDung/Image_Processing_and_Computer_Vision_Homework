import cv2
import os

# --- TỰ ĐỘNG TÌM ĐƯỜNG DẪN CHUẨN ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_bai3")
os.makedirs(output_dir, exist_ok=True)

img_path = os.path.join(current_dir, "images", "pic_week1.jpg")

# --- 1. ĐỌC ẢNH VÀ GIẢM KÍCH THƯỚC BẰNG SLICING ---
img = cv2.imread(img_path)

if img is None:
    print(f"Lỗi: Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn: {img_path}")
    exit()

img_half = img[::2, ::2]
img_quarter = img[::4, ::4]

# --- LƯU KẾT QUẢ ---
path_original = os.path.join(output_dir, 'img_original.jpg')
path_half = os.path.join(output_dir, 'img_half.jpg')
path_quarter = os.path.join(output_dir, 'img_quarter.jpg')

cv2.imwrite(path_original, img)
cv2.imwrite(path_half, img_half)
cv2.imwrite(path_quarter, img_quarter)

# --- IN THÔNG SỐ SHAPE ---
print("--- THÔNG SỐ SHAPE (KÍCH THƯỚC MA TRẬN) ---")
print(f"Ảnh gốc (1/1) : {img.shape}")
print(f"Ảnh giảm 1/2  : {img_half.shape}")
print(f"Ảnh giảm 1/4  : {img_quarter.shape}")

# --- 2. SO SÁNH DUNG LƯỢNG FILE (KB) ---
size_original = os.path.getsize(path_original) / 1024
size_half = os.path.getsize(path_half) / 1024
size_quarter = os.path.getsize(path_quarter) / 1024

print("\n--- SO SÁNH DUNG LƯỢNG FILE ---")
print(f"Dung lượng ảnh gốc : {size_original:.2f} KB")
print(f"Dung lượng ảnh 1/2 : {size_half:.2f} KB")
print(f"Dung lượng ảnh 1/4 : {size_quarter:.2f} KB")
print(f"-> Đã lưu thành công vào thư mục: {output_dir}/")
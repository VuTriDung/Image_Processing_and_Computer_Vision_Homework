import cv2
import numpy as np
import os

# --- TẠO THƯ MỤC CHỨA KẾT QUẢ ---
output_dir = "output_bai2"
os.makedirs(output_dir, exist_ok=True)

# --- HÀM TỰ CÀI ĐẶT ĐỂ ĐẢM BẢO GIÁ TRỊ [0, 255] ---
def clip_uint8(arr):
    # np.clip sẽ ép các số < 0 thành 0, và các số > 255 thành 255
    # Sau đó astype(np.uint8) để đưa ma trận về đúng chuẩn hiển thị ảnh
    return np.clip(arr, 0, 255).astype(np.uint8)

# --- 1. ĐỌC ẢNH VÀ CHỈNH SÁNG / TỐI / TƯƠNG PHẢN ---
# Đọc trực tiếp ảnh vào hệ Grayscale (1 kênh màu) để tiện làm toán
gray = cv2.imread('images/pic_week1.jpg', cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("Lỗi: Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn.")
    exit()

# Nếu lấy ảnh gốc (đang là uint8) trừ trực tiếp đi 50, 
# những pixel có giá trị < 50 (ví dụ 10) sẽ bị quay vòng thành 216 thay vì âm.
# Do đó, BẮT BUỘC phải chuyển ma trận sang dạng số thực (float) trước khi làm toán.
gray_float = gray.astype(np.float32)

# Làm toán trên ma trận
gray_dark = clip_uint8(gray_float - 50)       # Trừ đi 50 điểm sáng
gray_bright = clip_uint8(gray_float + 50)     # Cộng thêm 50 điểm sáng
gray_contrast = clip_uint8(gray_float * 1.5)  # Nhân hệ số 1.5 để dãn khoảng cách sáng/tối

# --- 2. TỰ CÀI ĐẶT THRESHOLD NHỊ PHÂN ---
T = 128
# Hàm np.where hoạt động như câu lệnh IF:
# Nếu pixel >= T thì gán bằng 255 (Trắng), ngược lại gán bằng 0 (Đen)
binary = np.where(gray >= T, 255, 0).astype(np.uint8)

# --- LƯU ẢNH RA THƯ MỤC ---
cv2.imwrite(os.path.join(output_dir, 'gray_original.png'), gray)
cv2.imwrite(os.path.join(output_dir, 'gray_dark.png'), gray_dark)
cv2.imwrite(os.path.join(output_dir, 'gray_bright.png'), gray_bright)
cv2.imwrite(os.path.join(output_dir, 'gray_contrast.png'), gray_contrast)
cv2.imwrite(os.path.join(output_dir, 'binary_threshold.png'), binary)

# --- 3. IN SO SÁNH GIÁ TRỊ PIXEL ---
# Chọn một tọa độ [y, x] bất kỳ để soi (Ví dụ dòng 100, cột 100)
row, col = 100, 100

print(f"--- SO SÁNH PIXEL TẠI TỌA ĐỘ [{row}, {col}] ---")
print(f"Giá trị ảnh gốc        : {gray[row, col]}")
print(f"Giá trị ảnh tối hơn    : {gray_dark[row, col]}")
print(f"Giá trị ảnh sáng hơn   : {gray_bright[row, col]}")
print(f"Giá trị ảnh tương phản : {gray_contrast[row, col]}")
print(f"Giá trị ảnh nhị phân   : {binary[row, col]}")
print(f"-> Đã lưu các ảnh thành công vào thư mục: {output_dir}/")
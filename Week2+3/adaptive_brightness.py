import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def process_single_image(img_name):
    """Xử lý ảnh, in ra Terminal và trả về toàn bộ thông số để vẽ lên giao diện"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(current_dir, "images", img_name)
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Lỗi: Không tìm thấy ảnh tại {img_path}")
        return None, None, "Error", 0, 0, 0

    # --- AUTO-DETECT ---
    mean_intensity = np.mean(img)
    std_intensity = np.std(img)
    bright_pixels_ratio = np.sum(img > 240) / img.size

    status = ""
    corrected_img = None

    if mean_intensity < 80:
        status = "Too Dark"
        gamma = 0.4
        corrected_img = np.clip(255 * (img / 255.0) ** gamma, 0, 255).astype(np.uint8)

    elif std_intensity < 50:
        status = "Low Contrast"
        corrected_img = cv2.equalizeHist(img)
        
    elif mean_intensity > 140 or bright_pixels_ratio > 0.05: 
        status = "Too Bright"
        gamma = 2.0
        corrected_img = np.clip(255 * (img / 255.0) ** gamma, 0, 255).astype(np.uint8)
        
    else:
        status = "Normal"
        corrected_img = img.copy()

    # GIỮ LẠI DỮ LIỆU TRÊN TERMINAL
    print(f"[{img_name}] Chẩn đoán: {status} | Mean: {mean_intensity:.1f}, Std: {std_intensity:.1f}, Bright Ratio: {bright_pixels_ratio:.2%}")
    
    # Trả về thêm các con số thống kê
    return img, corrected_img, status, mean_intensity, std_intensity, bright_pixels_ratio


# --- GOM TẤT CẢ VÀO MỘT BẢNG 3 HÀNG 4 CỘT ---
image_files = ['dark.jpg', 'low_contrast.jpg', 'bright.jpg']

# Tăng kích thước cửa sổ để có đủ không gian ghi chữ
plt.figure(figsize=(18, 12))

for i, img_name in enumerate(image_files):
    img, corrected_img, status, mean, std, b_ratio = process_single_image(img_name)
    
    if img is None:
        continue

    base_pos = i * 4

    # 1. Ảnh gốc + HIỂN THỊ SỐ LIỆU NGAY TRÊN TITLE
    plt.subplot(3, 4, base_pos + 1)
    
    # Gom text lại thành 2 dòng, tô màu đỏ đậm cho dễ nhìn
    info_title = (f"[{status}] - {img_name}\n"
                  f"Mean: {mean:.1f} | Std: {std:.1f} | Cháy sáng: {b_ratio:.1%}")
    plt.title(info_title, fontsize=11, color='darkred', fontweight='bold')
    
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    # 2. Histogram gốc
    plt.subplot(3, 4, base_pos + 2)
    plt.title("Original Histogram")
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
    plt.xlim([0, 256])

    # 3. Ảnh đã sửa
    plt.subplot(3, 4, base_pos + 3)
    plt.title("Corrected Image")
    plt.imshow(corrected_img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')

    # 4. Histogram đã sửa
    plt.subplot(3, 4, base_pos + 4)
    plt.title("Corrected Histogram")
    plt.hist(corrected_img.ravel(), bins=256, range=[0, 256], color='black')
    plt.xlim([0, 256])

# Tăng pad=3.0 để chữ của hàng trên không bị rớt đè xuống hình của hàng dưới
plt.tight_layout(pad=3.0) 
plt.show()
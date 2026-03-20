import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def process_single_image(img_path, output_dir):
    """Xử lý 1 ảnh bất kỳ, lưu kết quả và trả về thông số"""
    img_name = os.path.basename(img_path)
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

    # Xuất ảnh đã sửa
    out_name = f"corrected_{img_name}"
    cv2.imwrite(os.path.join(output_dir, out_name), corrected_img)

    print(f"[{img_name}] Chẩn đoán: {status} | Mean: {mean_intensity:.1f}, Std: {std_intensity:.1f}, Cháy sáng: {bright_pixels_ratio:.2%}")
    
    return img, corrected_img, status, mean_intensity, std_intensity, bright_pixels_ratio


def process_and_visualize_set(input_folder, output_folder, image_filenames, plot_name):
    """Hàm đa năng: Nhận danh sách ảnh, xử lý toàn bộ và xuất ra một Bảng Dashboard"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    in_dir = os.path.join(current_dir, input_folder)
    out_dir = os.path.join(current_dir, output_folder)
    os.makedirs(out_dir, exist_ok=True)
    
    num_images = len(image_filenames)
    if num_images == 0:
        print(f"Không có ảnh nào trong thư mục {input_folder}")
        return
        
    # Chiều cao bảng tự động co giãn theo số lượng ảnh (mỗi ảnh cao 4 inch)
    plt.figure(figsize=(18, 4 * num_images))
    
    for i, img_name in enumerate(image_filenames):
        img_path = os.path.join(in_dir, img_name)
        img, corrected_img, status, mean, std, b_ratio = process_single_image(img_path, out_dir)
        
        if img is None:
            continue

        base_pos = i * 4

        # 1. Ảnh gốc
        plt.subplot(num_images, 4, base_pos + 1)
        info_title = (f"[{status}] - {img_name}\n"
                      f"Mean: {mean:.1f} | Std: {std:.1f} | Cháy sáng: {b_ratio:.1%}")
        plt.title(info_title, fontsize=11, color='darkred', fontweight='bold')
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        # 2. Histogram gốc
        plt.subplot(num_images, 4, base_pos + 2)
        plt.title("Original Histogram")
        plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
        plt.xlim([0, 256])

        # 3. Ảnh đã sửa
        plt.subplot(num_images, 4, base_pos + 3)
        plt.title("Corrected Image")
        plt.imshow(corrected_img, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        # 4. Histogram đã sửa
        plt.subplot(num_images, 4, base_pos + 4)
        plt.title("Corrected Histogram")
        plt.hist(corrected_img.ravel(), bins=256, range=[0, 256], color='black')
        plt.xlim([0, 256])

    plt.tight_layout(pad=3.0) 
    plot_path = os.path.join(out_dir, plot_name)
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"-> Đã lưu bảng Dashboard vào: {plot_path}\n")
    plt.show()


# ==========================================
# --- CHƯƠNG TRÌNH CHÍNH ---
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))

# 1. CHẠY BỘ 3 ẢNH CỐ ĐỊNH (TEST CHUẨN)
print("=== XỬ LÝ BỘ ẢNH CHUẨN (Thư mục 'images') ===")
fixed_images = ['dark.jpg', 'low_contrast.jpg', 'bright.jpg']
process_and_visualize_set("images", "output_P1", fixed_images, "histograms_visualization.png")

# 2. CHẠY BỘ ẢNH RANDOM TỰ ĐỘNG
print("=== XỬ LÝ BỘ ẢNH NGẪU NHIÊN (Thư mục 'random_images') ===")
random_dir = os.path.join(current_dir, "random_images")

if os.path.exists(random_dir):
    # Quét tự động tất cả các file ảnh có trong thư mục
    random_images = [f for f in os.listdir(random_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    process_and_visualize_set("random_images", "output_random_P1", random_images, "random_histograms_visualization.png")
else:
    print(f"Chưa tạo thư mục '{random_dir}'. Bỏ qua phần test ngẫu nhiên.")
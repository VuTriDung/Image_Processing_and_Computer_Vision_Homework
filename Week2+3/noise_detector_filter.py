import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# 1. CÁC HÀM TẠO NHIỄU GIẢ LẬP
# ==========================================
def add_gaussian_noise(image, mean=0, std=25):
    row, col = image.shape
    gauss = np.random.normal(mean, std, (row, col))
    noisy = np.clip(image + gauss, 0, 255).astype(np.uint8)
    return noisy

def add_salt_and_pepper_noise(image, prob=0.04):
    noisy = np.copy(image)
    num_salt = np.ceil(prob * image.size * 0.5)
    num_pepper = np.ceil(prob * image.size * 0.5)
    
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[tuple(coords)] = 255
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[tuple(coords)] = 0
    return noisy

# ==========================================
# 2. HÀM AI NHẬN DIỆN VÀ LỌC NHIỄU
# ==========================================
def detect_and_filter_noise(noisy_img, clean_img, img_name, noise_category_name, output_dir):
    # --- AUTO-DETECT (LOGIC MỚI CHUẨN XÁC HƠN) ---
    # Đếm tỷ lệ pixel bị cháy đen (0) hoặc cháy trắng tuyệt đối (255)
    sp_pixels = np.sum((noisy_img == 0) | (noisy_img == 255))
    sp_ratio = sp_pixels / noisy_img.size

    # Nếu có trên 1% pixel bị cực đoan -> Chắc chắn là Salt & Pepper
    if sp_ratio > 0.01: 
        noise_type = "Salt-and-Pepper"
        filtered_img = cv2.medianBlur(noisy_img, 3)
        filter_applied = "Median Filter"
    else: 
        # Ngược lại là Gaussian
        noise_type = "Gaussian"
        filtered_img = cv2.bilateralFilter(noisy_img, d=9, sigmaColor=75, sigmaSpace=75)
        filter_applied = "Bilateral Filter"

    # Tính PSNR
    psnr_noisy = cv2.PSNR(clean_img, noisy_img)
    psnr_filtered = cv2.PSNR(clean_img, filtered_img)
    improvement = psnr_filtered - psnr_noisy

    # --- XUẤT ẢNH KẾT QUẢ RA FILE RỜI ---
    # Tạo tên file an toàn (bỏ dấu cách, dấu hai chấm)
    safe_category = noise_category_name.replace(":", "").replace(" ", "_")
    out_filename = f"filtered_{noise_type}_{safe_category}_{img_name}"
    cv2.imwrite(os.path.join(output_dir, out_filename), filtered_img)

    return noise_type, filter_applied, filtered_img, psnr_noisy, psnr_filtered, improvement


# ==========================================
# 3. CHƯƠNG TRÌNH CHÍNH & VẼ GIAO DIỆN
# ==========================================
def process_p3(img_name, output_dir):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(current_dir, "images", img_name)
    
    clean_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if clean_img is None:
        print(f"Lỗi: Không tìm thấy ảnh tại {img_path}")
        return

    noisy_images = {
        "True Noise: Gaussian": add_gaussian_noise(clean_img),
        "True Noise: Salt & Pepper": add_salt_and_pepper_noise(clean_img, prob=0.04)
    }

    plt.figure(figsize=(16, 10))
    plt.suptitle(f"Noise Type Detector & Filter Report - {img_name}", fontsize=16, fontweight='bold')

    row = 1
    for title, noisy_img in noisy_images.items():
        # Đưa thêm thông tin tên ảnh và output_dir vào để hàm tự động lưu file
        detected_type, filter_used, filtered_img, p_noise, p_filt, p_imp = \
            detect_and_filter_noise(noisy_img, clean_img, img_name, title, output_dir)
        
        # 1. Ảnh nhiễu
        plt.subplot(2, 3, (row-1)*3 + 1)
        plt.title(f"Input: {title}\nPSNR vs Clean: {p_noise:.2f} dB", color='darkred')
        plt.imshow(noisy_img, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        # 2. Histogram
        plt.subplot(2, 3, (row-1)*3 + 2)
        # Đổi màu xanh cho dễ nhận biết AI đã chẩn đoán đúng
        plt.title(f"Detected: {detected_type}\nApplied: {filter_used}", color='blue', fontweight='bold')
        plt.hist(noisy_img.ravel(), bins=256, range=[0, 256], color='gray')
        plt.xlim([0, 256])

        # 3. Ảnh đã lọc
        plt.subplot(2, 3, (row-1)*3 + 3)
        plt.title(f"Filtered Image\nPSNR: {p_filt:.2f} dB (+{p_imp:.2f} dB)", color='green')
        plt.imshow(filtered_img, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')
        
        row += 1

    plt.tight_layout()
    report_path = os.path.join(output_dir, f"P3_Report_{img_name.split('.')[0]}.png")
    plt.savefig(report_path, dpi=150, bbox_inches='tight')
    print(f"-> Đã lưu báo cáo và ảnh rời của {img_name} vào {output_dir}/")
    plt.show()

# --- CHẠY TOOL ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_P3")
os.makedirs(output_dir, exist_ok=True)

test_images = ['img_p3_1.jpg', 'img_p3_2.jpg']
for img in test_images:
    process_p3(img, output_dir)
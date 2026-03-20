import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from scipy import signal

def get_gaussian_kernel_2d(kernel_size, sigma=0):
    """Tạo ma trận bộ lọc Gaussian 2D chuẩn"""
    if sigma == 0:
        sigma = 0.3 * ((kernel_size - 1) * 0.5 - 1) + 0.8
    k1d = cv2.getGaussianKernel(kernel_size, sigma)
    k2d = np.outer(k1d, k1d)
    return k2d

def process_and_benchmark(img_name, kernel_size, output_dir):
    """Đua tốc độ và trả về kết quả cho 1 ảnh"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(current_dir, "images", img_name)
    
    img_color = cv2.imread(img_path)
    if img_color is None:
        print(f"Lỗi: Không tìm thấy ảnh {img_path}")
        return None
    
    img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    
    # --- BƯỚC 1: CẮT GÓC ẢNH 100x100 ĐỂ ĐUA TỐC ĐỘ ---
    h, w = img_gray.shape
    start_y, start_x = h // 2 - 50, w // 2 - 50
    crop_100x100 = img_gray[start_y:start_y+100, start_x:start_x+100]
    
    kernel = get_gaussian_kernel_2d(kernel_size)
    
    print(f"\n[{img_name}] Đang test tốc độ với Kernel Size: {kernel_size}x{kernel_size}...")
    
    # Test Spatial
    start_time = time.perf_counter()
    signal.convolve(crop_100x100, kernel, mode='same', method='direct')
    spatial_time = time.perf_counter() - start_time
    
    # Test FFT
    start_time = time.perf_counter()
    signal.convolve(crop_100x100, kernel, mode='same', method='fft')
    fft_time = time.perf_counter() - start_time
    
    # --- BƯỚC 2: CHỌN PHƯƠNG PHÁP NHANH HƠN ---
    if spatial_time < fft_time:
        chosen_method = 'direct'
        method_name = 'Spatial'
    else:
        chosen_method = 'fft'
        method_name = 'FFT'

    print(f" - Thời gian Spatial : {spatial_time:.6f} giây")
    print(f" - Thời gian FFT     : {fft_time:.6f} giây")
    print(f" => TỰ ĐỘNG CHỌN: {method_name}")
    
    # --- BƯỚC 3: ÁP DỤNG LÊN TOÀN BỘ ẢNH ---
    print(f"Đang làm mờ toàn bộ ảnh bằng {method_name}... (Đợi vài giây nhé)")
    blurred_img = np.zeros_like(img_color)
    full_start = time.perf_counter()
    
    for c in range(3):
        blurred_channel = signal.convolve(img_color[:,:,c], kernel, mode='same', method=chosen_method)
        blurred_img[:,:,c] = np.clip(blurred_channel, 0, 255)
        
    full_time = time.perf_counter() - full_start
    print(f"Hoàn thành trong {full_time:.2f} giây!")
    
    # Lưu file kết quả
    out_bgr = cv2.cvtColor(blurred_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(output_dir, f"blurred_{kernel_size}_{img_name}"), out_bgr)
    
    return img_color, blurred_img, spatial_time, fft_time, method_name

# ==========================================
# --- CHƯƠNG TRÌNH CHÍNH ---
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output_P2")
os.makedirs(output_dir, exist_ok=True)

test_cases = [
    ('img_p2_1.jpg', 11),  # Ảnh 1 test với kernel nhỏ
    ('img_p2_2.jpg', 81)   # Ảnh 2 test với kernel khổng lồ
]

results = []
for img_name, k_size in test_cases:
    res = process_and_benchmark(img_name, k_size, output_dir)
    if res is not None:
        # res = (img_color, blurred_img, spatial_time, fft_time, method_name, k_size)
        results.append((*res, k_size, img_name))

# --- VẼ GIAO DIỆN BÁO CÁO (2 HÀNG x 2 CỘT) ---
if results:
    plt.figure(figsize=(15, 12))
    
    for i, (orig, blurred, sp_time, fft_time, method, k_size, img_name) in enumerate(results):
        base_pos = i * 2
        
        # Ảnh gốc
        plt.subplot(len(results), 2, base_pos + 1)
        plt.title(f"Original: {img_name}", fontsize=13)
        plt.imshow(orig)
        plt.axis('off')
        
        # Ảnh đã làm mờ + Thông số benchmark
        plt.subplot(len(results), 2, base_pos + 2)
        info_title = (f"Blurred (Kernel: {k_size}x{k_size})\n"
                      f"Auto-selected: {method}\n"
                      f"Benchmark: Spatial {sp_time:.5f}s | FFT {fft_time:.5f}s")
        
        plt.title(info_title, fontsize=12, color='darkred', fontweight='bold')
        plt.imshow(blurred)
        plt.axis('off')
        
    plt.tight_layout(pad=3.0)
    report_path = os.path.join(output_dir, "combined_benchmark_report.png")
    plt.savefig(report_path, dpi=150, bbox_inches='tight')
    print(f"\n-> Đã lưu bảng báo cáo vào: {report_path}")
    
    # Hiển thị lên màn hình
    plt.show()
# 📚 Bài Tập Tuần 2+3: Các thuật toán nâng cao & Bộ nhận diện tự động (Advanced Algorithms & Auto-Detectors)
Đây là phân hệ cốt lõi của đồ án, nơi các thuật toán xử lý ảnh kinh điển được kết hợp với logic thống kê để tạo ra các hệ thống **Auto-Detectors** (Nhận diện & Xử lý tự động).

---

## 📝 Bài P1: Bộ điều chỉnh độ sáng thích ứng (Adaptive Brightness Adjuster)
**Thử thách thiết kế:** Xây dựng một công cụ tự động sửa các bức ảnh bị thiếu sáng/dư sáng (cháy sáng).

**Yêu cầu:**
* **Đầu vào (Input):** Bất kỳ ảnh đa cấp xám nào (không biết trước mức độ phơi sáng).
* **Tự động nhận diện (Auto-detect):** Ảnh quá tối? Quá sáng? Hay độ tương phản thấp? *(Sử dụng dữ liệu thống kê biểu đồ Histogram)*.
* **Tự động sửa lỗi (Auto-correct):** Áp dụng phép biến đổi phù hợp:
  * Nếu ảnh tối $\rightarrow$ Hiệu chỉnh Gamma ($\gamma < 1$)
  * Nếu ảnh sáng $\rightarrow$ Hiệu chỉnh Gamma ngược ($\gamma > 1$)
  * Nếu độ tương phản thấp $\rightarrow$ Cân bằng Histogram (Histogram equalization) hoặc Kéo giãn độ tương phản (Contrast stretching)
* **Đầu ra (Output):** Ảnh đã được sửa lỗi + Bảng trực quan hóa (visualization) hiển thị biểu đồ Histogram trước/sau khi sửa.

---

## 📝 Bài P2: Bộ lựa chọn thuật toán làm mờ thông minh (Smart Blur Selector)
**Thử thách thiết kế:** Xây dựng một công cụ áp dụng bộ lọc làm mờ Gaussian một cách hiệu quả, tự động chọn phương pháp trong miền không gian (Spatial) hoặc miền tần số (FFT).

**Yêu cầu:**
* **Đầu vào (Input):** Bức ảnh + kích thước ma trận làm mờ (kernel size) mong muốn.
* **Tự động chọn phương pháp (Auto-select method):**
  * Đo thời gian chạy của phép tích chập không gian (Spatial convolution) trên một vùng ảnh cắt kích thước $100 \times 100$.
  * Đo thời gian chạy của phương pháp FFT trên cùng vùng ảnh cắt đó.
  * Chọn phương pháp chạy nhanh hơn để áp dụng cho toàn bộ bức ảnh gốc.
* **Đầu ra (Output):** Ảnh đã làm mờ + Báo cáo hiển thị:
  * Phương pháp được chọn (Spatial hoặc FFT)
  * Thời gian thực thi (Execution time)
  * Lý do *(Ví dụ: "FFT được chọn vì kích thước kernel 81 lớn hơn điểm giao cắt 31")*

---

## 📝 Bài P3: Bộ nhận diện & Lọc loại nhiễu (Noise Type Detector & Filter)
**Thử thách thiết kế:** Xây dựng một công cụ tự động nhận diện loại nhiễu và áp dụng bộ lọc tối ưu nhất.

**Yêu cầu:**
* **Đầu vào (Input):** Ảnh đa cấp xám bị nhiễu (không biết trước loại nhiễu).
* **Tự động nhận diện loại nhiễu (Auto-detect noise type):**
  * Tính toán biểu đồ Histogram và các chỉ số thống kê (tỷ lệ điểm dị biệt - outlier ratio, hình dáng phân bố).
  * Phân loại thành: Nhiễu hạt (Gaussian), Nhiễu muối tiêu (Salt-and-pepper), hoặc loại khác.
* **Tự động chọn bộ lọc (Auto-select filter):**
  * Nếu là nhiễu Gaussian $\rightarrow$ Dùng bộ lọc làm mờ Gaussian (Gaussian blur) hoặc Lọc song phương (Bilateral filter).
  * Nếu là nhiễu muối tiêu $\rightarrow$ Dùng bộ lọc trung vị (Median filter).
* **Đầu ra (Output):** Ảnh đã được lọc + Báo cáo hiển thị:
  * Loại nhiễu được phát hiện
  * Bộ lọc được áp dụng
  * Độ cải thiện PSNR *(Nếu có sẵn ảnh gốc sạch để đối chiếu)*

## 📁 Chi tiết các hệ thống (Projects)

### 1. Exercise P1: Adaptive Brightness Adjuster
**File thực thi:** `adaptive_brightness.py`

Hệ thống phân tích biểu đồ Histogram và các chỉ số thống kê cục bộ để tự động "bắt bệnh" về phơi sáng của ảnh và áp dụng thuật toán cứu sáng phù hợp.
* **Auto-Detect Logic:**
  * Nếu $\text{Mean} < 80$: Chẩn đoán **Too Dark**.
  * Nếu $\text{Std} < 50$: Chẩn đoán **Low Contrast** (Mù mịt).
  * Nếu $\text{Mean} > 140$ hoặc tỷ lệ pixel $> 240$ vượt $5\%$: Chẩn đoán **Too Bright** (Cháy sáng/Ngược sáng).
* **Thuật toán áp dụng:**
  * **Gamma Correction:** Sử dụng hàm biến đổi phi tuyến tính $V_{out} = c \cdot V_{in}^\gamma$. Với ảnh tối, áp dụng $\gamma = 0.4$ để kéo giãn vùng tối. Với ảnh sáng, áp dụng $\gamma = 2.0$ để nén vùng lóa.
  * **Histogram Equalization (`cv2.equalizeHist`):** Kéo giãn dải phân bố pixel để tăng độ tương phản cho ảnh mù mịt.
* **Output:** Tạo thư mục `output_P1/`, xuất ảnh riêng lẻ và bảng Report Dashboard gồm 3 ảnh + 6 Histogram so sánh.

---

### 2. Exercise P2: Smart Blur Selector
**File thực thi:** `smart_blur_selector.py`

Một công cụ Benchmark tự động đánh giá và lựa chọn thuật toán làm mờ tối ưu nhất dựa trên định lý Tích chập (Convolution Theorem).
* **Vấn đề lý thuyết:** Tích chập trong miền không gian (Spatial) có độ phức tạp $\mathcal{O}(M^2 N^2)$, rất chậm với ma trận (kernel) lớn. Biến đổi Fourier (FFT) chuyển tích chập thành phép nhân ma trận với độ phức tạp $\mathcal{O}(MN \log(MN))$, nhanh hơn cực nhiều ở kernel lớn nhưng lại có độ trễ khởi tạo ở kernel nhỏ.
* **Auto-Select Logic:**
  * Trích xuất (crop) ngẫu nhiên một vùng $100 \times 100$ pixel từ ảnh gốc.
  * Cho 2 thuật toán chạy đua nghiệm thu thời gian thực (Benchmark) trên vùng ảnh này bằng `scipy.signal.convolve`.
  * Thuật toán nào trả kết quả nhanh hơn sẽ được hệ thống tự động khóa mục tiêu và áp dụng cho toàn bộ bức ảnh độ phân giải cao.
* **Output:** Tạo thư mục `output_P2/`, xuất ảnh đã làm mờ cùng Dashboard ghi nhận thời gian đua tốc độ của Spatial vs FFT.

---

### 3. Exercise P3: Noise Type Detector & Filter
**File thực thi:** `noise_detector_filter.py`

Một "Bác sĩ đa khoa" chuyên nhận diện loại nhiễu phá hoại bức ảnh và tự động bốc đúng loại thuốc lọc phù hợp.
* **Tạo dữ liệu thử nghiệm:** Tự động tiêm 2 loại nhiễu vào ảnh sạch: Nhiễu hạt (Gaussian Noise) và Nhiễu muối tiêu (Salt & Pepper Noise).
* **Auto-Detect Logic:**
  * Đếm số lượng các pixel mang giá trị cực đoan ($0$ hoặc $255$). 
  * Nếu tỷ lệ này $> 1\%$, hệ thống khẳng định đây là nhiễu **Salt-and-Pepper**. Nếu không, nó là nhiễu **Gaussian**.
* **Thuật toán áp dụng (Auto-Filter):**
  * *Salt-and-Pepper:* Sử dụng **Median Filter** (Lọc trung vị) để nuốt trọn các điểm dị biệt trắng/đen mà không làm mờ ảnh.
  * *Gaussian:* Sử dụng **Bilateral Filter** (Lọc song phương) thay vì Gaussian Blur thông thường. Bilateral Filter bảo toàn hoàn hảo các đường viền (edges) trong khi làm mịn các vùng nhiễu đồng nhất.
* **Đánh giá hiệu năng:** Đo lường sự cải thiện chất lượng ảnh trước và sau khi lọc bằng chỉ số **PSNR** (Peak Signal-to-Noise Ratio). Điểm $+dB$ càng cao chứng tỏ thuật toán khôi phục càng tốt.
* **Output:** Tạo thư mục `output_P3/`, xuất 4 ảnh kết quả đã lọc và Dashboard báo cáo phát hiện nhiễu.
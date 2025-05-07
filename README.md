# Tra Cứu Phạt Nguội Tự Động

Dự án này tự động tra cứu thông tin phạt nguội phương tiện giao thông từ trang web [Cục Cảnh Sát Giao Thông](https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html). Dự án sử dụng Selenium để tự động hóa trình duyệt, Tesseract OCR để giải mã captcha, và thư viện `schedule` để chạy định kỳ.

---

## 1. Yêu cầu hệ thống

### Phần mềm:

- Python 3.8 trở lên
- Google Chrome (phiên bản mới nhất)
- ChromeDriver (phiên bản tương thích với Google Chrome)

### Thư viện Python:

- `selenium`
- `pytesseract`
- `opencv-python`
- `numpy`
- `Pillow`
- `schedule`
- `python-dotenv`

### Công cụ OCR:

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (cài đặt trên hệ thống)

---

## 2. Hướng dẫn cài đặt

### Bước 1: Clone dự án

```bash
git clone https://github.com/Thanhhoai230504/BT_Lon_TDH.git
cd BT_LON_TDH
```

### Bước 2: Cài đặt môi trường Python

1. Tạo môi trường ảo:

   ```bash
   python -m venv venv
   ```

2. Kích hoạt môi trường ảo:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```

3. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

### Bước 3: Cài đặt Tesseract OCR

1. Tải và cài đặt Tesseract OCR từ [tesseract-ocr](https://github.com/tesseract-ocr/tesseract).
2. Sau khi cài đặt, xác định đường dẫn đến file thực thi `tesseract.exe`. Thông thường, đường dẫn sẽ là:
   ```
   C:\Program Files\Tesseract-OCR\tesseract.exe
   ```
3. Cập nhật đường dẫn này trong file `Phat_Nguoi.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### Bước 4: Cài đặt ChromeDriver

1. Tải ChromeDriver từ [trang chính thức](https://chromedriver.chromium.org/downloads).
2. Đảm bảo phiên bản ChromeDriver tương thích với phiên bản Google Chrome đang cài đặt.
3. Thêm đường dẫn ChromeDriver vào biến môi trường `PATH` hoặc đặt ChromeDriver trong cùng thư mục với dự án.

### Bước 5: Cấu hình biến môi trường

1. Tạo file `.env` trong thư mục gốc của dự án:
   ```bash
   touch .env
   ```
2. Thêm biển số xe cần tra cứu vào file `.env`:
   ```
   bien_so=30A12345
   ```

---

## 3. Hướng dẫn sử dụng

### Chạy tra cứu thủ công

1. Chạy file `Phat_Nguoi.py` để tra cứu thông tin phạt nguội:
   ```bash
   python Phat_Nguoi.py
   ```

### Chạy tra cứu định kỳ

1. Chạy file `schedule_tra_cuu.py` để tự động tra cứu theo lịch:
   ```bash
   python schedule_tra_cuu.py
   ```
2. Mặc định, chương trình sẽ tra cứu vào các thời điểm được cấu hình trong file:
   ```python
   schedule.every().day.at("11:28").do(job_tra_cuu)
   schedule.every().day.at("11:29").do(job_tra_cuu)
   ```

---

## 4. Cấu trúc dự án

```
tra-cuu-phat-nguoi/
│
├── Phat_Nguoi.py          # Chứa logic tra cứu và xử lý captcha
├── schedule_tra_cuu.py    # Chạy tra cứu định kỳ
├── .env                   # File cấu hình biển số xe
├── requirements.txt       # Danh sách thư viện cần cài đặt
└── README.md              # Hướng dẫn sử dụng
```

---

## 5. Ghi chú

- Đảm bảo kết nối internet ổn định khi chạy chương trình.
- Nếu gặp lỗi liên quan đến ChromeDriver, hãy kiểm tra phiên bản ChromeDriver và Google Chrome để đảm bảo chúng tương thích.

---

## 6. Liên hệ

Nếu bạn gặp vấn đề hoặc cần hỗ trợ, vui lòng liên hệ qua email: `nguyenthanhhoai230504@gmail.com`.

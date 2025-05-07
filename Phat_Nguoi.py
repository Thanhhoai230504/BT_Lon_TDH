from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import pytesseract
import numpy as np
import cv2
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img):
    img = img.convert("L") 
    img = np.array(img)
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    img = cv2.bilateralFilter(img, 11, 17, 17)
    img = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        21, 10
    )
    kernel = np.ones((2, 2), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.bitwise_not(img)

    return img

def tra_cuu_phat_nguoi(bien_so):
    driver = webdriver.Chrome()
    #1. Vào website đã chọn.
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

    while True:
        try:
            #2. Nhập các thông tin Biển số xe
            input_bien_so = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "BienKiemSoat")))
            input_bien_so.clear()
            input_bien_so.send_keys(bien_so)

            #3. Chọn loại xe.
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="formBSX"]/div[2]/div[2]/select'))).click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="formBSX"]/div[2]/div[2]/select/option[2]'))).click()

            #4. Lấy hình captcha và xử lý để lấy mã capchat.
            captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "imgCaptcha")))
            captcha_png = captcha_img.screenshot_as_png 
            img = Image.open(BytesIO(captcha_png))  
            img_processed = preprocess_image(img)  

            captcha_code = pytesseract.image_to_string(
                img_processed,
                config='--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            ).strip()

            print(f"[Captcha OCR]: {captcha_code}")

            #5. Nhập mã captcha vào ô 
            captcha_input = driver.find_element(By.NAME, "txt_captcha")
            captcha_input.clear()
            captcha_input.send_keys(captcha_code)

            driver.find_element(By.CLASS_NAME, "btnTraCuu").click()

            time.sleep(5)  

            try:
                error_elem = driver.find_element(By.XPATH, '//*[@id="formBSX"]/div[2]/div[4]')
                if "Mã xác nhận sai" in error_elem.text:
                    print("Captcha sai! Reload lại trang và thử lại...")
                    driver.refresh()
                    time.sleep(2)
                    continue  
            except:
                pass  
            #6. Kiểm tra kết quả phạt nguội.
            try:
                xpath_result = '//*[@id="bodyPrint123"]'
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_result)))  
                element_result = driver.find_element(By.XPATH, xpath_result)
                
                if "Không tìm thấy kết quả" in element_result.text:
                    print("Không tìm thấy vi phạm phạt nguội")
                else:
                    print("Tìm thấy vi phạm phát nguội")
            except:
                print("Không tìm thấy kết quả hoặc trang không phản hồi.")

            break 
        except Exception as e:
            print(f"Lỗi xảy ra: {e}")
            driver.refresh()
            time.sleep(2)

    time.sleep(3)
    driver.quit()






import schedule
import time
from Phat_Nguoi import tra_cuu_phat_nguoi  
from dotenv import load_dotenv
import os

load_dotenv()
bienso = os.getenv("bien_so")

def job_tra_cuu():
    bien_so = bienso
    tra_cuu_phat_nguoi(bien_so)
    print(f"Đã tra cứu vi phạm xe {bien_so}")

# Set lịch chạy 6h sáng và 12h trưa hằng ngày.
schedule.every().day.at("06:00").do(job_tra_cuu)
schedule.every().day.at("12:00").do(job_tra_cuu)

print("Hệ thống tra cứu đã sẵn sàng chạy lúc 6h và 12h mỗi ngày...")

while True:
    schedule.run_pending()
    time.sleep(60)

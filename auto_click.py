from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# 设置无头浏览器参数
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 创建 Service 对象，适配新版 Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 日志文件
log_file = "click_log.txt"

try:
    driver.get("https://onlyno999.streamlit.app/")
    time.sleep(10)  # 等待页面加载

    # 查找按钮
    buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'get this app back up')]")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if buttons:
        buttons[0].click()
        log_entry = f"[{timestamp}] 按钮已点击\n"
        print("检测到按钮，已点击。")
    else:
        log_entry = f"[{timestamp}] 未发现按钮，未执行点击\n"
        print("未检测到按钮，跳过。")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

except Exception as e:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] 错误：{str(e)}\n")
    print(f"发生错误：{e}")

finally:
    driver.quit()

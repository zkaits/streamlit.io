from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import time

# 设置 Chrome 浏览器选项
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 初始化 WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# 日志文件路径
log_file = "click_log.txt"

try:
    # 打开网页
    driver.get("https://onlyno999.streamlit.app/")
    time.sleep(10)  # 等待页面加载，可调整

    # 查找并点击按钮
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'get this app back up')]")
    button.click()

    # 记录时间
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] 点击成功\n"

    # 写入日志
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print("点击完成，已记录日志。")

except Exception as e:
    # 出错时也写入日志
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] 点击失败：{str(e)}\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"发生错误：{e}")

finally:
    driver.quit()

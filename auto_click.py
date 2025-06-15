from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# 设置 Chrome 浏览器为无头模式
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 初始化 Chrome 驱动
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# 日志文件路径
log_file = "click_log.txt"

try:
    # 打开网页
    driver.get("https://onlyno999.streamlit.app/")
    time.sleep(10)  # 等待页面加载完成

    # 查找包含特定文本的按钮
    buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'get this app back up')]")

    # 获取当前时间
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if buttons:
        buttons[0].click()
        log_entry = f"[{timestamp}] 按钮已点击\n"
        print("检测到按钮，已点击。")
    else:
        log_entry = f"[{timestamp}] 未发现按钮，未执行点击\n"
        print("未检测到按钮，跳过。")

    # 写入日志
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

except Exception as e:
    # 出错时记录
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] 错误：{str(e)}\n")
    print(f"发生错误：{e}")

finally:
    driver.quit()

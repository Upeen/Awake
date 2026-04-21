from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import requests
import os

# 🔗 YOUR STREAMLIT APPS
URLS = [
    "https://youtube-kh6rosxefwmjzgadaq7i9q.streamlit.app/",
    "https://contenthindinews-ncirgqofw4tgg8vveurmty.streamlit.app/"
]

LOG_FILE = "keep_alive.log"

# 🔔 OPTIONAL TELEGRAM ALERT
BOT_TOKEN = ""   # add if needed
CHAT_ID = ""     # add if needed

def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {message}"
    
    print(line)
    
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def send_alert(message):
    if BOT_TOKEN and CHAT_ID:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except:
            pass

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def is_sleeping(page_source):
    keywords = ["sleep", "waking", "starting", "app is sleeping"]
    return any(k in page_source.lower() for k in keywords)

def ping_apps():
    log("🚀 Starting keep-alive job")

    success_count = 0
    fail_count = 0

    driver = create_driver()

    for url in URLS:
        try:
            log(f"🌐 Checking: {url}")
            driver.get(url)
            time.sleep(5)

            page = driver.page_source

            if is_sleeping(page):
                log(f"😴 Sleeping detected: {url}")
                log("🔄 Waking app...")
                driver.refresh()
                time.sleep(25)

            else:
                log(f"⚡ Already active: {url}")
                time.sleep(10)

            success_count += 1

        except Exception as e:
            error_msg = f"❌ Error with {url}: {e}"
            log(error_msg)
            send_alert(error_msg)
            driver.save_screenshot("error.png")
            fail_count += 1

        time.sleep(5)

    driver.quit()

    log(f"📊 Summary: {success_count} success, {fail_count} failed")
    log("🏁 Finished job\n")


if __name__ == "__main__":
    ping_apps()

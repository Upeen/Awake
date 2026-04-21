from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# 🔗 YOUR STREAMLIT APPS
URLS = [
    "https://youtube-kh6rosxefwmjzgadaq7i9q.streamlit.app/",
    "https://contenthindinews-ncirgqofw4tgg8vveurmty.streamlit.app/"
]

LOG_FILE = "keep_alive.log"

def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {message}"
    
    print(line)  # shows in GitHub logs
    
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def ping_apps():
    log("🚀 Starting keep-alive job")

    driver = create_driver()

    for url in URLS:
        try:
            log(f"🌐 Visiting: {url}")
            driver.get(url)
            time.sleep(20)  # wait for full load
            log(f"✅ Success: {url}")
        except Exception as e:
            log(f"❌ Error with {url}: {e}")

        time.sleep(5)

    driver.quit()
    log("🏁 Finished keep-alive job\n")

if __name__ == "__main__":
    ping_apps()

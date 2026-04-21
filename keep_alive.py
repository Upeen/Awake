from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

URLS = [
    "https://youtube-kh6rosxefwmjzgadaq7i9q.streamlit.app/",
    "https://contenthindinews-ncirgqofw4tgg8vveurmty.streamlit.app/"
]

LOG_FILE = "keep_alive.log"

def log(status, url):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} | {url} | {status}"
    
    print(line)
    
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

def is_sleeping(page_source):
    keywords = ["sleep", "waking", "starting", "app is sleeping"]
    return any(k in page_source.lower() for k in keywords)

def ping_apps():
    driver = create_driver()

    for url in URLS:
        try:
            driver.get(url)
            time.sleep(5)

            page = driver.page_source

            if is_sleeping(page):
                log("SLEEP → REBUILD STARTED", url)

                driver.refresh()
                time.sleep(25)

                log("REBUILD SUCCESS", url)

            else:
                log("AWAKE", url)
                time.sleep(10)

        except Exception as e:
            log(f"ERROR: {e}", url)

        time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    ping_apps()

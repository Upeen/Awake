import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import concurrent.futures
import requests

# Get URLs from environment variables (comma-separated), fallback to default if not set
DEFAULT_URLS = "https://youtube-kh6rosxefwmjzgadaq7i9q.streamlit.app/,https://contenthindinews-ncirgqofw4tgg8vveurmty.streamlit.app/"
url_env = os.environ.get("TARGET_URLS", DEFAULT_URLS)
URLS = [url.strip() for url in url_env.split(",") if url.strip()]

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

LOG_FILE = "keep_alive.log"

def send_telegram_alert(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"Telegram alert failed: {e}")

def log(status, url):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} | {url} | {status}"
    
    print(line)
    
    # Write to log and keep only last 50 lines to prevent bloat
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
        else:
            lines = []
            
        lines.append(line + "\n")
        lines = lines[-50:] # Keep only last 50 lines
        
        with open(LOG_FILE, "w") as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Log error: {e}")

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

def ping_url(url):
    driver = None
    try:
        driver = create_driver()
        driver.set_page_load_timeout(30)
        driver.get(url)
        time.sleep(5) # Initial wait for content to start loading

        page = driver.page_source

        if is_sleeping(page):
            log("SLEEP → REBUILD STARTED", url)
            # Streamlit auto-reloads, wait for it
            time.sleep(25)
            log("REBUILD SUCCESS (Hopefully)", url)
        else:
            log("AWAKE", url)

    except Exception as e:
        error_msg = f"ERROR: {str(e)[:100]}..."
        log(error_msg, url)
        send_telegram_alert(f"🚨 Streamlit App Down!\nURL: {url}\nError: {error_msg}")
        # Take screenshot on error
        try:
            if driver:
                safe_name = "".join([c for c in url if c.isalpha() or c.isdigit()]).rstrip()
                filename = f"error_{safe_name[-20:]}.png"
                driver.save_screenshot(filename)
                log(f"Screenshot saved to {filename}", url)
        except Exception as ss_e:
            log(f"Screenshot failed: {ss_e}", url)

    finally:
        if driver:
            driver.quit()

def ping_apps():
    if not URLS:
        print("No URLs configured. Exiting.")
        return
        
    print(f"Pinging {len(URLS)} apps concurrently...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(ping_url, URLS)

if __name__ == "__main__":
    ping_apps()

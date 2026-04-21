from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 🔗 ADD YOUR STREAMLIT URLS HERE
URLS = [
    "https://youtube-kh6rosxefwmjzgadaq7i9q.streamlit.app/",
    # "https://your-second-app.streamlit.app/",
    # "https://your-third-app.streamlit.app/"
]

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def ping_apps():
    driver = create_driver()

    for url in URLS:
        try:
            print(f"🌐 Visiting: {url}")
            driver.get(url)
            time.sleep(20)  # wait for full load
            print(f"✅ Success: {url}")
        except Exception as e:
            print(f"❌ Error with {url}: {e}")

        time.sleep(5)  # small gap between apps

    driver.quit()

if __name__ == "__main__":
    ping_apps()

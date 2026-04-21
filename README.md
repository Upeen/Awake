# 🚀 Streamlit Keep-Alive Bot (Free & Open Source)

Keep your Streamlit apps awake 24/7 using **Selenium + GitHub Actions** — no server required.

---

## 🌟 Features

* 🔁 Automatic keep-alive (cron-based)
* 🌐 Supports multiple Streamlit apps
* 🤖 Uses real browser (Selenium) — reliable
* 🆓 100% free (uses GitHub Actions)
* ⚡ Easy setup (5 minutes)
* 🧩 Fully customizable

---

## 📁 Project Structure

```
streamlit-keepalive/
│
├── keep_alive.py          # Main script
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── keepalive.yml          # Automation workflow
```

---

## ⚙️ How It Works

1. GitHub Actions runs on a schedule
2. Python script launches a headless browser
3. Visits your Streamlit app(s)
4. Keeps them active (prevents sleep)

---

## 🚀 Setup Guide

### 1. Fork or Clone this Repository

```bash
git clone https://github.com/your-username/streamlit-keepalive.git
```

---

### 2. Add Your Streamlit URLs

Edit `keep_alive.py`:

```python
URLS = [
    "https://your-app.streamlit.app/",
    "https://another-app.streamlit.app/"
]
```

---

### 3. Push to GitHub

```bash
git add .
git commit -m "Setup keep alive"
git push
```

---

### 4. Enable GitHub Actions

* Go to **Actions tab**
* Click **Enable workflows**

---

## ⏱ Schedule Configuration

Default:

```yaml
cron: "*/30 * * * *"
```

Examples:

* Every 15 minutes → `"*/15 * * * *"`
* Every hour → `"0 * * * *"`

---

## 🧠 Why Selenium?

Streamlit requires a **real browser session**.

| Method          | Works |
| --------------- | ----- |
| curl / requests | ❌     |
| Selenium        | ✅     |

---

## ⚠️ Limitations

* GitHub Actions free tier:

  * ~2000 minutes/month
* Streamlit may still restart occasionally
* Not a replacement for paid hosting

---

## 🔧 Customization Ideas

* 🔔 Add Telegram/Email alerts
* 📊 Add logging dashboard
* ⚡ Parallel browser sessions
* 🔁 Retry failed requests
* 🌍 Proxy support

---

## 🐛 Troubleshooting

### App still sleeps?

* Increase frequency to 15 min
* Increase `time.sleep()` to 20 seconds

### Selenium errors?

* Ensure Chrome is installed via workflow
* Check logs in Actions tab

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to improve or extend features.

---

## 📜 License

MIT License — free to use and modify.

---

## ⭐ Support

If this helped you:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share it

---

## 💡 Author

Built to keep Streamlit apps alive without paying for hosting 🚀

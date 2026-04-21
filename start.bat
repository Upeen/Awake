@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Starting keep-alive script...
python keep_alive.py
pause

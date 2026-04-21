import time
import logging

# Constants for overall status
AWAKE = 'AWAKE'
SLEEP = 'SLEEP'
ERROR = 'ERROR'

# Configure logging
logging.basicConfig(filename='keep_alive.log', level=logging.INFO, format='%(message)s')

log_entries = []

# Function to log status
def log_status(url, status, overall_status):
    global log_entries
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} | {url} | {status} | {overall_status}"
    log_entries.append(log_entry)
    logging.info(log_entry)

    # Keep only the last 100 log entries
    if len(log_entries) > 100:
        log_entries = log_entries[-100:]

# Example usage
# log_status('http://example.com', AWAKE, AWAKE)
# log_status('http://example.com', SLEEP, SLEEP)
# log_status('http://example.com', ERROR, ERROR)
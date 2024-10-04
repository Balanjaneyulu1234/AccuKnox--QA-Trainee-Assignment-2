import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
PROCESS_THRESHOLD = 100  # number of processes

# Function to get current CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Function to get current memory usage
def check_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

# Function to get current disk usage
def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

# Function to get the number of running processes
def check_running_processes():
    process_count = len(psutil.pids())
    return process_count

# Function to log alerts
def log_alert(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_message = f"[{timestamp}] ALERT: {message}"
    
    # Log to console
    print(alert_message)
    
    # Optionally log to a file
    with open("system_health_log.txt", "a") as log_file:
        log_file.write(alert_message + "\n")

# Function to monitor the system health
def monitor_system_health():
    # Check CPU usage
    cpu_usage = check_cpu_usage()
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

    # Check memory usage
    memory_usage = check_memory_usage()
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")

    # Check disk space usage
    disk_usage = check_disk_usage()
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"Low disk space: {disk_usage}% used")

    # Check number of running processes
    process_count = check_running_processes()
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"Too many running processes: {process_count} processes")

# Main function to run the monitoring script
if __name__ == "__main__":
    # You can schedule this to run periodically, e.g., in a loop or as a cron job
    monitor_system_health()

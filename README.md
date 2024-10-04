##1.System Health Monitoring Script: 
Develop a script that monitors the health of a Linux system. It should check

CPU usage, memory usage, disk space, and running processes. If any of

these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the

script should send an alert to the console or a log file.To develop a system health monitoring script for Linux, we can use Python to gather key system metrics like CPU usage, memory usage, disk space, and running processes using the `psutil` library. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script will log an alert or print it to the console.

### Prerequisites:

1. **Install psutil**: You’ll need the `psutil` library to access system resource usage. You can install it via pip:
   ```bash
   pip install psutil
   ```

### System Health Monitoring Script


    

# Main function to run the monitoring script
if __name__ == "__main__":
    # You can schedule this to run periodically, e.g., in a loop or as a cron job

### Key Features of the Script:

1. **CPU Usage**:
   - The `psutil.cpu_percent(interval=1)` function checks CPU usage over a 1-second interval.

2. **Memory Usage**:
   - `psutil.virtual_memory().percent` gives the percentage of memory currently used.

3. **Disk Usage**:
   - `psutil.disk_usage('/')` returns the disk usage statistics for the root directory (`/`), showing the percentage of disk space used.

4. **Process Count**:
   - `len(psutil.pids())` provides the number of currently running processes.

5. **Logging Alerts**:
   - If any of these metrics exceed predefined thresholds (CPU > 80%, Memory > 80%, Disk Usage > 80%, or Running Processes > 100), the script generates an a
3. Run the script:
   ```bash
   python system_health_monitor.py
   ```

### Automating with Cron:

To make this script run periodically (e.g., every 5 minutes), you can set it up as a cron job:

1. Open the cron job editor:
   ```bash
   crontab -e
   ```
2. Add the following line to run the script every 5 minutes:
   ```bash
   */5 * * * * /usr/bin/python3 /path/to/system_health_monitor.py
   ```

### Customization:

- **Email Alerts**: You can modify the `log_alert` function to send an email alert instead of just logging to a file. Use Python’s `smtplib` or integrate with an external service like SendGrid or AWS SES.
- **Extended Monitoring**: You can add more metrics, such as network traffic or I/O stats, by using other functions from `psutil` (e.g., `psutil.net_io_counters()`).


###2.Automated Backup Solution:

Write a script to automate the backup of a specified directory to a remote

server or a cloud storage solution. The script should provide a report on the

success or failure of the backup operation.
This script will help you proactively monitor the system’s health and catch potential performance or resource issues in a Linux environment.
To automate the backup of a directory to a remote server or cloud storage solution, you can use Python with the `subprocess` module for system commands like `rsync` (for remote servers) or APIs (for cloud storage). This script will back up a directory to a remote server via SSH using `rsync` and generate a report on the success or failure of the operation.

### Automated Backup Script Using `rsync`

The following script will:

1. Compress the specified directory.
2. Transfer it to a remote server using `rsync` over SSH.
3. Provide a report on whether the backup was successful or failed.

#### Prerequisites:

- **Rsync**: Ensure `rsync` is installed (`rsync` is commonly available on most Linux/Mac systems).
- **SSH Key Authentication**: Ensure SSH access to the remote server is set up without needing a password (i.e., using an SSH key).
- **Python**: Make sure you have Python installed.

#### Python Backup Script:


### Explanation:

1. **Compression**:
   - The script first compresses the specified directory into a `.tar.gz` archive using the `tar` command. The resulting backup file will be named based on the current timestamp, ensuring no overwriting of previous backups.

2. **File Transfer**:
   - The script uses `rsync` over SSH to transfer the compressed backup file to the remote server (`/backup` directory on the remote host).
   - Ensure you have set up passwordless SSH login using SSH keys on the remote host for seamless automation.

3. **Backup Report**:
   - After the backup operation (whether successful or not), the script generates a report containing the timestamp, source directory, and the status of the operation (success or failure).
   - The report is printed to the console and also appended to a `backup_report.txt` file.

### Running the Script:

1. Save the script as `backup_script.py`.
2. Update the following variables:
   - `source_directory`: The directory you want to back up.
   - `local_backup_dir`: Where the local compressed backup files should be stored.
   - `remote_server`: The remote server address where backups will be transferred.
   - `remote_username`: Your SSH username for the remote server.
3. Ensure that `/backup` exists on your remote server or adjust the destination directory as needed.
4. Run the script:
   ```bash
   python backup_script.py
   ```

### Customization:

- **Cloud Storage**: If you want to back up to cloud storage like AWS S3 or Google Cloud Storage, you can modify the script to use cloud SDKs (like `boto3` for AWS or `google-cloud-storage` for GCP).
- **Automate with Cron**: You can schedule this backup script to run periodically by adding it to a cron job. For example, to run it daily at midnight, add this line to your cron jobs:
  ```bash
  0 0 * * * /usr/bin/python3 /path/to/backup_script.py
  ```

This solution will automate backups and provide status reporting, which is useful for monitoring and ensuring data integrity over time.


###3.Log File Analyzer:
Create a script that analyzes web server logs (e.g., Apache, Nginx) for
common patterns such as the number of 404 errors, the most requested
pages, or IP addresses with the most requests. The script should output a
summarized report.
To create a log file analyzer for web server logs (e.g., Apache or Nginx), we can use Python to parse the log file, extract useful information such as the number of 404 errors, most requested pages, and IP addresses with the most requests, and then generate a summarized report.

### Example Script to Analyze Web Server Logs

Here’s a sample Python script to achieve this:


### Key Features of the Script:

1. **Log File Parsing**:
   - The script uses regular expressions to parse each log line based on a common Apache/Nginx log format. It extracts the IP address, request method, request path, status code, and other information from the log file.

2. **Status Code Counting**:
   - It tracks how many times each HTTP status code appears, focusing on the number of `404` errors.

3. **Page Requests**:
   - It counts how many times each page (request path) is accessed.

4. **IP Address Tracking**:
   - The script identifies which IP addresses made the most requests.

5. **Summarized Report**:
   - It generates a report showing:
     - The number of `404` errors.
     - The top 5 most requested pages.
     - The top 5 IP addresses making the most requests.

### Running the Script:

1. Save the script as `log_analyzer.py`.
2. Update the `log_file_path` variable to point to the location of your web server’s access log file.
3. Run the script:
   ```bash
   python log_analyzer.py
   ```

### Example Log Entry (for Apache/Nginx):

Here’s a typical log line for Apache or Nginx:

```
127.0.0.1 - - [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1234
```

- **IP Address**: `127.0.0.1`
- **Timestamp**: `10/Oct/2024:13:55:36 +0000`
- **HTTP Method**: `GET`
- **Request Path**: `/index.html`
- **HTTP Status Code**: `200`
- **Response Size**: `1234` bytes

### Customization:

- You can extend the script to capture other log information (e.g., user agents, response times).
- Add more functionality, such as generating a CSV report or emailing the summary to administrators.

This script will help you monitor key metrics and troubleshoot potential issues based on web server logs.


###4.Application Health Checker:Please write a script that can check the uptime of an application and 
determine if it is functioning correctly or not. The script must accurately

assess the application's status by checking HTTP status codes. It should be

able to detect if the application is 'up', meaning it is functioning correctly, or

'down', indicating that it is unavailable or not responding.
To create a simple health checker script that checks the uptime of an application by evaluating HTTP status codes, you can use Python with the `requests` library. Below is an example script that checks the application's health by sending a GET request to the specified URL and checking the response status code.

### Prerequisites
Make sure you have Python installed along with the `requests` library. You can install the `requests` library using pip if you haven't already:

```bash
pip install requests
```

### Health Checker Script

Here's a sample Python script for the health checker:


### Explanation

- **Importing Libraries**: The script starts by importing the `requests` library for handling HTTP requests.
- **Function `check_application_health`**: This function takes a URL as an argument and performs the following:
  - Sends a GET request to the specified URL.
  - Checks the response status code:
    - If the status code is `200`, it indicates the application is functioning correctly.
    - If the status code is anything else, it indicates the application is down or experiencing issues.
  - If there's an exception (e.g., connection error), it catches it and prints an error message indicating the application is down.
- **Main Section**: This is where you specify the URL of your application that you want to check.

### Running the Script
To run the script, save it to a file named `health_checker.py` and execute it:

```bash
python health_checker.py
```

### Customization
- You can modify the `application_url` variable to point to your application’s health endpoint.
- You can expand the functionality to check additional status codes or implement logging for better monitoring. 

This script will provide a basic health check for your application, allowing you to monitor its uptime effectively.

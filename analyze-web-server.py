import re
from collections import defaultdict

# Function to analyze the web server log file
def analyze_log_file(log_file):
    # Regex pattern for common Apache/Nginx log format
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[^\]]+)\] "(?P<method>\w+) (?P<path>[^ ]+) HTTP/\d+\.\d+" (?P<status>\d+) (?P<bytes>\d+)'
    )

    # Initialize counters and data holders
    status_count = defaultdict(int)
    page_requests = defaultdict(int)
    ip_requests = defaultdict(int)

    # Open and read the log file
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                
                # Count status codes
                status = data['status']
                status_count[status] += 1

                # Track page requests
                page = data['path']
                page_requests[page] += 1

                # Track IP address requests
                ip = data['ip']
                ip_requests[ip] += 1

    # Generate summarized report
    generate_report(status_count, page_requests, ip_requests)

# Function to generate and display the report
def generate_report(status_count, page_requests, ip_requests):
    print("\n--- Log File Analysis Report ---\n")

    # 404 Errors
    print(f"Number of 404 Errors: {status_count.get('404', 0)}\n")

    # Most Requested Pages
    print("Top 5 Most Requested Pages:")
    for page, count in sorted(page_requests.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"{page}: {count} requests")

    print("\n")

    # IP Addresses with the Most Requests
    print("Top 5 IP Addresses with Most Requests:")
    for ip, count in sorted(ip_requests.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"{ip}: {count} requests")

# Main execution
if __name__ == "__main__":
    # Path to the web server log file
    log_file_path = "access.log"  # Update this to the actual path of your log file

    analyze_log_file(log_file_path)

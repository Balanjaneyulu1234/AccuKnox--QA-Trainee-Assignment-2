import os
import subprocess
import datetime

# Function to create a backup of the specified directory
def backup_directory(source_dir, backup_dir, remote_host, remote_user):
    # Get current date and time for timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"{backup_dir}/backup_{timestamp}.tar.gz"

    try:
        # Compress the directory into a tar.gz file
        print(f"Compressing {source_dir} into {backup_file}...")
        subprocess.run(['tar', '-czf', backup_file, '-C', os.path.dirname(source_dir), os.path.basename(source_dir)], check=True)
        print(f"Directory compressed successfully: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compress the directory: {e}")
        return False

    try:
        # Use rsync to transfer the backup file to the remote server
        print(f"Transferring {backup_file} to {remote_user}@{remote_host}:/backup...")
        subprocess.run(['rsync', '-avz', backup_file, f'{remote_user}@{remote_host}:/backup'], check=True)
        print(f"Backup transferred successfully to {remote_host}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to transfer the backup: {e}")
        return False

# Function to generate a backup report
def generate_report(success, source_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if success:
        report = f"Backup Successful!\nTime: {timestamp}\nSource Directory: {source_dir}\n"
    else:
        report = f"Backup Failed!\nTime: {timestamp}\nSource Directory: {source_dir}\n"
    
    # Print report
    print("\n--- Backup Report ---")
    print(report)

    # Optionally, you can save this report to a file or send an email
    with open("backup_report.txt", "a") as report_file:
        report_file.write(report)

if __name__ == "__main__":
    # Define source directory and backup parameters
    source_directory = "/path/to/source/directory"  # Update to the directory you want to back up
    local_backup_dir = "/path/to/local/backup"      # Update to where compressed files should be saved
    remote_server = "your.remote-server.com"        # Remote server address
    remote_username = "username"                   # Username for the remote server

    # Ensure the backup directory exists
    if not os.path.exists(local_backup_dir):
        os.makedirs(local_backup_dir)

    # Run the backup process
    backup_success = backup_directory(source_directory, local_backup_dir, remote_server, remote_username)
    
    # Generate a report
    generate_report(backup_success, source_directory)

import os
import subprocess
import zipfile

def gather_system_logs():
    # Define the paths and filenames
    logs_directory = "/var/log"  # Directory containing system logs
    zip_filename = "system_logs.zip"

    # Get a list of log files in the logs_directory
    log_files = [os.path.join(logs_directory, filename) for filename in os.listdir(logs_directory) if os.path.isfile(os.path.join(logs_directory, filename))]

    # Create a zip file to store the logs
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for log_file in log_files:
            # Add each log file to the zip file
            zipf.write(log_file, os.path.basename(log_file))

if __name__ == "__main__":
    try:
        gather_system_logs()
        print("System logs have been gathered and saved as 'system_logs.zip'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

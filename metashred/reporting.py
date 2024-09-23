# Imports

import os
import time

# Real Time Reports

def real_time_output(operation_type, path, passes=0):
    
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    size = os.path.getsize(path) if os.path.isfile(path) else "N/A"

    if operation_type == "file":
        print(f"[{timestamp}] Deleted file: {path} | Size: {size} bytes | Passes: {passes}")
    elif operation_type == "directory":
        print(f"[{timestamp}] Deleted directory: {path}")
    elif operation_type == "metadata":
        print(f"[{timestamp}] Wiped metadata of: {path} | Passes: {passes}")
    else:
        print(f"[{timestamp}] Unknown operation on: {path}")

# Summary Reports


class SummaryReport:
    # Group of functions that make possible track the files, directories and errors retrieved by the program 
    def __init__(self):
        self.wiped_files = []
        self.wiped_directories = []
        self.errors = []
    
    def track_file_wipe(self, file_path):
        self.wiped_files.append(file_path)

    def track_directory_wipe(self, directory_path):
        self.wiped_directories.append(directory_path)

    def track_error(self, error_message):
        self.errors.append(error_message)

    def print_summary(self):
        print("\nSummary Report:")
        print("--------------------------")
        
        print(f"Total files wiped: {len(self.wiped_files)}")
        for current_file in self.wiped_files:
            print(f"- {current_file}")

        print(f"Total directories wiped: {len(self.wiped_directories)}")
        for directory in self.wiped_directories:
            print(f"- {directory}")

        if self.errors:
            print("\nErrors encountered:")
            for error in self.errors:
                print(f"- {error}")
        else:
            print("\nNo errors encountered.")
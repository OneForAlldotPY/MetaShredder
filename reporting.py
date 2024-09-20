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

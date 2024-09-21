import random
import os
import shutil
import file_wipe
import reporting

def random_string(length=8):
    chars = 'abcdefghijklmnopqrstouvxwyz0123456789_-'
    return ''.join(random.choice(chars) for i in range(length))



def wipe_directory(directory, passes=3):
    """Securely wipe a directory by wiping its metadata and then deleting it."""
    try:
        # First, recursively wipe all files and subdirectories
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                # Delegate file wiping to the file_wipe.py logic (which will be imported in main.py)
                file_wipe.wipe_file(file_path, passes)
            elif os.path.isdir(file_path):
                # Recursively wipe subdirectories
                wipe_directory(file_path, passes)

        # After wiping contents, overwrite the directory's metadata
        wipe_directory_metadata(directory, passes)

        # Remove the directory itself
        shutil.rmtree(directory)
        reporting.real_time_output(operation_type="directory", path=directory)
        reporting.SummaryReport.track_directory_wipe(directory)
        

    except Exception as e:
        reporting.SummaryReport.track_error(f"Error wiping directory {directory}: {e}")
        print(f"Error wiping directory {directory}: {e}")

def wipe_directory_metadata(directory, passes=3):
    """Overwrite directory metadata to make it unrecoverable."""
    try:
        for _ in range(passes):
            new_name = os.path.join(os.path.dirname(directory), random_string(8))
            os.rename(directory, new_name)
            directory = new_name
        reporting.real_time_output(operation_type="metadata", path=directory, passes=passes)
    except Exception as e:
        reporting.SummaryReport.track_error(f"Error wiping directory metadata {directory}: {e}")
        print(f"Error wiping directory metadata {directory}: {e}")
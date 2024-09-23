import random
import os
import shutil
import metashred.file_wipe as file_wipe
import metashred.reporting as reporting

def random_string(length=8):
    chars = 'abcdefghijklmnopqrstouvxwyz0123456789_-'
    return ''.join(random.choice(chars) for i in range(length))



def wipe_directory(directory, passes=3, summary_report=None):
    """Securely wipe a directory by wiping its metadata and then deleting it."""
    try:
        # First, recursively wipe all files and subdirectories
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                # Delegate file wiping to the file_wipe.py logic (which will be imported in main.py)
                file_wipe.wipe_file(file_path, passes, summary_report)
            elif os.path.isdir(file_path):
                # Recursively wipe subdirectories
                wipe_directory(file_path, passes, summary_report)

        # After wiping contents, overwrite the directory's metadata
        new_directory = wipe_directory_metadata(directory, passes)

        # Remove the directory itself
        shutil.rmtree(new_directory)
        reporting.real_time_output(operation_type="directory", path=directory)
        
        if summary_report:
            summary_report.track_directory_wipe(new_directory)
        

    except Exception as e:
        error_message = f"Error wiping directory {directory}: {e}"
        print(error_message)
        if summary_report:
            summary_report.track_error(error_message)

def wipe_directory_metadata(directory, passes=3):
    """Overwrite directory metadata to make it unrecoverable."""
    try:
        for _ in range(passes):
            new_name = os.path.join(os.path.dirname(directory), random_string(8))
            os.rename(directory, new_name)
            directory = new_name
        reporting.real_time_output(operation_type="metadata", path=directory, passes=passes)
        return directory
    except Exception as e:
        error_message = f"Error wiping directory metadata {directory}: {e}"
        print(error_message)
        raise
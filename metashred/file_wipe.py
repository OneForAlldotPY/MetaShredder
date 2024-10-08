import os
import shutil
import random
import metashred.reporting as reporting

#Base pattern for the passes and overwritting
def overwrite_pattern(file_path, pattern, passes):
    try:
        with open(file_path, 'r+b') as f:
            length = os.path.getsize(file_path)
            for _ in range (passes):
                f.seek(0)
                f.write(pattern * length)
                f.flush()
                os.fsync(f.fileno()) 

    except Exception as e:
        reporting
        print(f"Error overwriting file {file_path}: {e}")


def wipe_file(file_path, passes=3, summary_report = None):
    
    patterns = [
        bytearray([0] * os.path.getsize(file_path)),
        bytearray([255] * os.path.getsize(file_path)),
        bytearray(random.getrandbits(8) for _ in range(os.path.getsize(file_path)))
    ]

    for pattern in patterns[:passes]:
        overwrite_pattern(file_path, pattern, 1)

    try:
        os.remove(file_path)
        reporting.real_time_output(operation_type="file", path=file_path, passes=passes)
        if summary_report:
            summary_report.track_file_wipe(file_path)
    except Exception as e:
        error_message = f"Error deleting file {file_path}: {e}"
        print(error_message)
        if summary_report:
            summary_report.track_error(error_message)


    
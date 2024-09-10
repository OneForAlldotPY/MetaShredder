import os
import shutil


#Base pattern for the passes and overwritting
def overwrite_pattern(file_path, pattern, passes):
    try:
        with open(file_path, 'r+b') as f:
            length = os.path.getsize(file_path)
            for i in range (passes):
                f.seek(0)
                f.write(pattern * length)
                f.flush
                os.fsync(f.fileno()) 

    except Exception as e:
        print(f"Error overwriting file {file_path}: {e}")

import os
import shutil
import random

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


def wipe_file(file_path, passes=3):
    patterns = [
        bytearray([0] * os.path.getsiz(file_path)),
        bytearray([255] * os.path.getsize(file_path)),
        bytearray(random.getrandbits(8) for i in range(os.path.getsize(file_path)))
    ]

    for pattern in patterns[:passes]:
        overwrite_pattern(file_path, pattern, 1)

    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
        
import platform
import subprocess
import os

os = platform.system()

def wipe_free_space(path):
    if os == "Windows":
        wipe_free_space_windows(path)
    elif os == "Linux":
        wipe_free_space_linux(path)
    else:
        print("Unsupported OS: {os}")


def wipe_free_space_windows(drive_letter):
    try:
        subprocess.run(['cipher', '/w:{}'.format(drive_letter)], check=True)
        print(f"Successfully wiped free space on drive {drive_letter} drive (Windows).")
    except subprocess.CalledProcessError as e:
        print(f"Error wiping free space on drive {drive_letter} drive: {e}")
    
def wipe_free_space_linux(path):
    zerofile_path = os.path.join(path, "zerofile")
    try:
        with open(zerofile_path, 'wb') as f:
            subprocess.run(['dd', 'if=/dev/zero', f'of={zerofile_path}'], check=True)
        os.remove(zerofile_path)
    except subprocess.CalledProcessError as e: 
        print(f"Error wiping free space: {e}")
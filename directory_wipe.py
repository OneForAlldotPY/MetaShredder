import random
import os

def random_string(length=8):
    chars = 'abcdefghijklmnopqrstouvxwyz0123456789_-'
    return ''.join(random.choice(chars) for i in range(length))



def wipe_directory(directory, passes=3):
    """Securely wipe a directory by wiping its metadata and then deleting it."""
    try:
        # Overwrite the directory's metadata (like its name) to make it unrecoverable
        wipe_directory_metadata(directory, passes)

        # Finally, remove the directory itself
        os.rmdir(directory)
    except Exception as e:
        print(f"Error handling directory {directory}: {e}")  



def wipe_directory_metadata(directory, passes=3):
    try:
        for _ in range(passes):
            new_name = os.path.join(os.path.dirname(directory), random_string(8))
            os.rename(directory, new_name)
            directory = new_name
    except Exception as e:
        print (f"Error wiping directory metadata {directory}: {e}")

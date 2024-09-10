#Imports
import os 
import argparse
import directory_wipe
import file_wipe

#Main function
def main():
    parser = argparse.ArgumentParser(description="Securely wipe files and directories.")
    parser.add_argument("path", help="Path to the file or directory to wipe.")
    parser.add_argument("--passes", type=int, default=3, help="Number of passes for overwriting files")

    args = parser.parse_args()

    path = args.path
    passes = args.passes

    if os.path.isfile(path):
        file_wipe.wipe_file(path, passes)
    elif os.path.isdir(path):
        directory_wipe.wipe_directory_metadata(path, passes)
        directory_wipe.wipe_directory(path, passes)
    else: 
        print(f"Error: {path} is neither a file or a directory.")

if __name__ == "__main__":
    main()
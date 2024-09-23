#Imports
import os 
import argparse
import directory_wipe
import file_wipe
import free_space_wipe
import reporting

#Main function

def deletion_confirmation():
    # Prompt the user for a confirmation before proceeding with the wiping process
    
    while True:
        response = input("This action will permanently delete files and directories on this path. Are you sure you want to proceed? (yes/no): ").strip().lower()
        if response in ("yes", "y"):
            return True
        elif response in ("no", "n"):
            print("Operation cancelled.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    parser = argparse.ArgumentParser(description="Securely wipe files and directories.")
    parser.add_argument("path", help="Path to the file or directory to wipe.")
    parser.add_argument("--passes", type=int, default=3, help="Number of passes for overwriting files")
    parser.add_argument("--wipe-free-space", action='store_true', help="Wipe the free space on the given path/drive")

    args = parser.parse_args()

    deletion_confirmation()

    path = args.path
    passes = args.passes
    report = reporting.SummaryReport()

    if os.path.isfile(path):
        file_wipe.wipe_file(path, passes, summary_report=report)

    elif os.path.isdir(path):
        directory_wipe.wipe_directory(path, passes, summary_report=report)
    else: 
        print(f"Error: {path} is neither a file or a directory.")
        return
    
    if args.wipe_free_space:
        free_space_wipe.wipe_free_space(path)

    report.print_summary()

if __name__ == "__main__":
    main()
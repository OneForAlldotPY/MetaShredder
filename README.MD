# MetaShredder

MetaShredder is a Python-based file and directory shredding tool designed to securely delete files, directories, and wipe free space. The tool ensures data is unrecoverable by overwriting file contents and metadata multiple times.

## Features

- Securely overwrite files and directories using multiple passes.
- Wipe free space on a drive to ensure deleted data cannot be recovered.
- Track wiped files, directories, and any errors with a summary report.
- Recursive directory wiping with metadata destruction.
- Works on Windows, macOS, and Linux.

## Installation

### Clone this repository:

```
git clone https://github.com/yourusername/metashredder.git
```

### Navigate to the project directory:

```
cd metashredder
```

No additional dependencies are required.

## Usage

MetaShredder is designed to be run from the command line. You can securely wipe files, directories, and free space by specifying the path and options.

## CLI Arguments
``path``: The path to the file or directory to be wiped.
``--passes``: Number of overwrite passes (default: 3).
``--wipe-free-space``: Option to wipe free space on the specified path or drive after the deletion.

### Example Commands

1. Wipe a File:

``python metashred.py "path/to/file.txt" --passes 3``

2. Wipe a Directory:

``python metashred.py "path/to/directory" --passes 5``

3. Run the program interactively: MetaShredder asks for confirmation before proceeding to wipe files:

``python metashred.py "path/to/directory"``


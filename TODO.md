NEXT STEPS


Dry Run Mode:
    Implement a mode that simulates, logs and retrieves the results of the wiping process without making actual changes;
    Provide feedback to the user of what would be done if the mode were not enabled.

Interactive Confirmation:
    Add a confirmation prompt before performing any destructive operations;
    Ensure that the confirmation is secure and clear to prevent accidental data loss.

Wiping Free Space:
    Implemnt a method to securely handle the wiping of free disk space in order to add another layer of preventing any recovery of preveously deleted files;
    Integrate this feature into the existing wiping process

Checksum Verification:
    Checksum implementation to ensure integrity of the wiped data;
    Add a flag to enable or disable checksum verification during the wiping process(or before it).

Selective Wiping Based On File Type:
    Choose to only wipe a certain file content/type/extension from a given directory
    

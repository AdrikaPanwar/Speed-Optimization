# System Speed Optimization Script 

This Python script performs essential maintenance tasks on a Linux system to enhance performance and speed. It includes functionalities to update the system, clean unnecessary packages, disable window animations, clear cache, and optimize the file system.

## Features

- **System Update**: Ensures all packages are up to date. 🔄
- **Package Cleanup**: Removes unnecessary packages and cleans the local repository.
- **Disable Animations**: Enhances performance by turning off window animations.
- **Cache Clearing**: Frees up RAM by clearing cached memory. 
- **File System Optimization**: Uses `e4defrag` to optimize the ext4 file system.
- **Disk Usage Check**: Displays total, used, and free disk space. 📊

## Requirements

- Python 3.x 🐍
- `apt` package manager
- `gsettings` for the GNOME desktop environment
- `e4defrag` for ext4 filesystem optimization

## How to Use

1. **Install Python**: Ensure Python 3 is installed on your system.
2. **Run the Script**:
   - Save the script as `optimize_speed.py`.
   - Open a terminal and navigate to the directory where the script is saved.
   - Execute the script using:
     ```bash
     python3 optimize_speed.py
     ```
   - You may be prompted to enter your password for `sudo` access. 

## Conclusion

This script helps maintain and improve the performance of your Linux system. By automating routine tasks, it ensures a smoother and more efficient user experience. 



import os
import subprocess

def update_system():
    print("Updating system...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

def clean_up():
    print("Cleaning up unnecessary packages...")
    subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
    subprocess.run(["sudo", "apt", "clean"], check=True)

def disable_animations():
    print("Disabling window animations...")
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "enable-animations", "false"], check=True)

def disable_unnecessary_services():
    # Keeping Bluetooth enabled by commenting out the line below
    services = [
        # "bluetooth.service",  # Commenting this line to keep Bluetooth enabled
        # Add more services here acc. to you
    ]
    for service in services:
        print(f"Disabling {service}...")
        subprocess.run(["sudo", "systemctl", "disable", service], check=True)

def clear_cache():
    print("Clearing system cache...")
    subprocess.run(["sudo", "sync"], check=True)
    subprocess.run(["sudo", "sysctl", "-w", "vm.drop_caches=3"], check=True)

def optimize_file_system():
    print("Optimizing file system...")
    subprocess.run(["sudo", "e4defrag", "/"], check=True)  # Optimize ext4 filesystem

def check_disk_usage():
    print("Checking disk usage...")
    total, used, free = os.popen("df -h /").read().splitlines()[1].split()[1:4]
    print(f"Total: {total}, Used: {used}, Free: {free}")

def main():
    update_system()
    clean_up()
    disable_animations()
    disable_unnecessary_services()
    clear_cache()
    optimize_file_system()
    check_disk_usage()
    print("Speed optimization complete!")

if __name__ == "__main__":
    main()

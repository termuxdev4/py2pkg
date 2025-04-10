import os  
import subprocess  
import shutil  
import sys  
  
def setup_pkg():  
    if len(sys.argv) < 2 or sys.argv[1] != "setup-pkg":  
        print("Usage: setup-pkg <package-name>")  
        sys.exit(1)  
  
    package_name = sys.argv[2] if len(sys.argv) > 2 else input("Package Name: ").strip()  
    source_file = input("Enter the source filename (e.g. script.py): ").strip()  
  
    if not os.path.isfile(source_file):  
        print("File not found.")  
        sys.exit(1)  
  
    with open(source_file, 'r') as f:  
        source_code = f.read()  
  
    description = input("Description: ").strip()  
    version = input("Version: ").strip()  
    maintainer = input("Maintainer: ").strip()  
    architecture = input("Architecture (usually 'all' or 'aarch64'): ").strip()  
  
    filename_no_ext = os.path.splitext(os.path.basename(source_file))[0]  
    home = os.path.expanduser("~")  
    package_dir = os.path.join(home, package_name)  
    bin_path = os.path.join(package_dir, "data/data/com.termux/files/usr/bin")  
  
    os.makedirs(bin_path, exist_ok=True)  
  
    script_path = os.path.join(bin_path, filename_no_ext)  
    with open(script_path, 'w') as f:  
        f.write(source_code)  
  
    subprocess.run(["chmod", "+x", script_path])  
  
    debian_dir = os.path.join(package_dir, "DEBIAN")  
    os.makedirs(debian_dir, exist_ok=True)  
  
    control_content = f"""Package: {package_name}  
Version: {version}  
Section: base  
Priority: optional  
Architecture: {architecture}  
Maintainer: {maintainer}  
Description: {description}  
"""  
    with open(os.path.join(debian_dir, "control"), 'w') as f:  
        f.write(control_content)  
  
    subprocess.run(["chmod", "0755", package_dir])  
    subprocess.run(["chmod", "0755", debian_dir])  
  
    print(f"Package directory structure created at: {package_dir}")  
    print(f"Permissions set: chmod 0755 {package_dir}")  
    print(f"Permissions set: chmod 0755 {debian_dir}")  
    print(f"To build the .deb package, run:")  
    print(f"dpkg-deb -b {package_dir}")  
  
if __name__ == "__main__":  
    setup_pkg()

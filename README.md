# Py2pkg - Python to Debian Package Converter  

## Overview  

Py2pkg is a utility tool designed to convert Python scripts into installable Debian packages (.deb) specifically tailored for the Termux environment. It automates the packaging process by generating proper directory structures, control files, and setting necessary permissions, allowing Python developers to easily distribute their scripts as standard packages.  

## Key Features  

- Automated Debian package creation from Python source files  
- Customizable package metadata (name, version, description, etc.)  
- Proper file structure generation for Termux compatibility  
- Permission handling for executable scripts  
- Simple command-line interface for quick packaging  
- Lightweight implementation with no external dependencies beyond standard tools  

## Installation  

To install py2pkg, execute the following command in your Termux environment:  

```bash  
wget https://raw.githubusercontent.com/termuxdev4/py2pkg/refs/heads/main/install.sh | bash  
```  

This installation script will:  
1. Install `wget` if not already present  
2. Download the latest py2pkg script  
3. Place it in your Termux binary directory (`/data/data/com.termux/files/usr/bin/`)  
4. Set executable permissions  
5. Confirm successful installation  

## Usage  

After installation, you can convert your Python script to a Debian package with:  

```bash  
py2pkg setup-pkg <package-name>  
```  

The tool will guide you through an interactive process to:  
1. Specify your Python source file  
2. Enter package metadata (description, version, maintainer, etc.)  
3. Set architecture compatibility  
4. Generate the complete package structure  

Once completed, you can build the `.deb` package with:  

```bash  
dpkg-deb -b <package-directory>  
```  

## Detailed Workflow  

1. **Source File Selection**  
   - The tool verifies the existence of your Python script and reads its contents.  

2. **Package Metadata Collection**  
   - Interactive prompts gather all necessary Debian control information, including:  
     - Package name  
     - Version number  
     - Maintainer information  
     - Architecture specification (`all`, `aarch64`, etc.)  
     - Detailed description  

3. **Directory Structure Creation**  
   - Generates standard Debian package directory layout  
   - Ensures Termux-compatible file paths (`/data/data/com.termux/files/usr/bin/`)  
   - Creates `DEBIAN/control` file with all metadata  

4. **File Placement**  
   - Copies your Python script to the correct binary directory  
   - Sets executable permissions (`chmod +x`)  

5. **Permission Setting**  
   - Applies appropriate permissions (`0755`) for the entire package directory  

## Technical Specifications  

- **Compatibility**: Designed specifically for Termux on Android  
- **Package Format**: Standard Debian `.deb` packages  
- **Dependencies**: Requires `dpkg-deb` for final package building  
- **License**: MIT  
- **Architectures Supported**: All architectures supported by Termux (`all`, `aarch64`, `arm`, `x86_64`, etc.)  

## Advanced Usage  

For experienced users, py2pkg supports direct command-line arguments to skip interactive prompts:  

```bash  
py2pkg setup-pkg <package-name> <source-file> <version> <maintainer> <architecture> <description>  
```  

All arguments after `<package-name>` are optional but must be provided in order if skipping interactivity.  

## Package Structure  

The generated package follows standard Debian conventions with Termux-specific paths:  

```  
<package-name>/  
├── DEBIAN/  
│   └── control  
└── data/data/com.termux/files/usr/bin/  
    └── <script-name>  
```  

## Building and Installing Packages  

After running py2pkg, the generated directory structure can be converted to a `.deb` package using:  

```bash  
dpkg-deb -b <package-directory>  
```  

This creates a standard Debian package that can be installed in Termux with:  

```bash  
dpkg -i <package-name>.deb  
```  

## License  

Py2pkg is released under the **MIT License**. See the `LICENSE` file in the project repository for full details.  

## Support  

For issues or feature requests, please open an issue on the project's GitHub repository. Contributions are welcome.

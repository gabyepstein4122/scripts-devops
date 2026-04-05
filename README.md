# System Maintenance Automation 🚀

This project provides an automated solution for system maintenance on Ubuntu/Debian-based distributions. It features a Python engine for cleanup tasks and a professional Bash installer to set up a `systemd` service that runs every time the system boots.

## ✨ Features
- **Automated Cleanup**: Clears `apt` cache and temporary files to keep your SSD lean.
- **Persistent Logging**: Tracks every execution in `maintenance.log` with timestamps.
- **Systemd Integration**: Runs as a background service on startup.
- **Portable Installer**: A one-click setup script that handles paths and permissions automatically.

## 🛠️ Project Structure
- `maintenance.py`: Core Python script that handles the maintenance logic.
- `maintenance.service`: Template for the Linux system service.
- `install.sh`: Automated Bash installer for easy deployment.

## 🚀 Getting Started

### Prerequisites
- Ubuntu/Debian-based Linux distribution.
- Python 3.x installed.

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gabyepstein4122/scripts-devops.git](https://github.com/gabyepstein4122/scripts-devops.git)
   cd scripts-devops

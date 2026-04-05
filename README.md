# DevOps & System Administration Toolkit 🛠️

A collection of automated tools and scripts designed to optimize, monitor, and maintain Linux-based environments (Ubuntu/Debian). This repository serves as a portfolio of Infrastructure as Code (IaC) and automation logic developed during my DevOps studies.

## 📂 Repository Structure

Each tool is contained within its own directory, including its specific logic and automated installer:

* **[system-maintenance/](./system-maintenance/)**: Automated system cleanup (apt, temp files) with `systemd` integration and logging.
* *Upcoming: battery-monitor*: Real-time battery health and status tracking.
* *Upcoming: network-status*: Diagnostic tools for connectivity and latency.

## 🚀 Design Principles
- **Portability**: Every tool includes an `install.sh` for one-click deployment.
- **Automation**: Focus on background services (systemd) to minimize manual tasks.
- **Observability**: Detailed logging for every automated action.

## 🛠️ Tech Stack
- **Languages**: Python 3.x, Bash Scripting.
- **Linux**: Systemd units, Crontab, Filesystem permissions.
- **Version Control**: Git (Feature-branch workflow).

## 👨‍💻 About the Author
I'm **Gabriel (Gaboa)**, a Tech Support specialist and DevOps student at the National University of Córdoba (**UNC**). Currently focusing on SRE, automation, and system optimization.

---
*Note: This is a work in progress as I transition into DevOps/SRE roles.*

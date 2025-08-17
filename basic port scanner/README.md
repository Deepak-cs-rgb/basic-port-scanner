# 🔍 Basic Port Scanner

A simple Python-based port scanner (like a lightweight Nmap) that scans open ports on a target host.  
Built with `socket` for networking fundamentals and can be extended with multi-threading, banner grabbing, and service detection.

## 🚀 Features
- Scans a range of ports on a target IP/hostname
- Detects open ports
- Simple command-line interface
- Timeout handling

## 🛠️ Skills Demonstrated
- Networking fundamentals (TCP, ports, sockets)
- Python programming
- Security tool development

## 📂 Project Structure
- `port_scanner.py` → Main scanner script
- `utils/services.py` → Common port-to-service mappings
- `results/scan_results.txt` → Stores scan results
- `requirements.txt` → Dependencies (none except Python standard library)

## ⚡ Usage
```bash
python port_scanner.py

# RAT Education Wardog 🐺

> **Educational Project** — This repository is designed for cybersecurity students and red teamers who want to understand how Remote Access Trojans (RATs) function in controlled, legal environments such as lab setups or virtual machines.  
> ⚠️ **DISCLAIMER:** This project is strictly for **educational and defensive security purposes only**. Do **not** use this code for unauthorized access or malicious activity. Doing so is illegal and punishable by law.

---

## 📌 Project Overview

This project demonstrates how a **basic Remote Access Trojan (RAT)** can be embedded into a macOS phishing-style application for **educational lab exercises**.  

The `rat.py` file is designed to automatically run in the background after installation, establishing a reverse shell connection to a Command & Control (C2) server (e.g., a Kali Linux VM).  

It’s a **fully functional example for learning** about:
- C2 connections over TCP
- Command execution and directory navigation
- Clipboard capture (macOS)
- File upload from the infected host to the C2

---

## ⚙️ Features

- ✅ Persistent reverse shell connection to a defined C2 host and port  
- 📂 Change directories, execute system commands remotely  
- 📝 Clipboard capture using AppleScript (macOS only)  
- 📡 File upload support (host to C2)  
- 🧠 Extensive logging for educational review and debugging

---

## 🧠 Educational Use Case

This RAT is typically **embedded inside the package contents** of a macOS `.app` phishing application.  
When the user installs or opens the app, the RAT script executes in the background and connects back to the attacker-controlled VM for demonstration in lab settings.  

This allows students and red teamers to:
- Observe real-time network connections
- Analyze reverse shell behavior using tools like Suricata, Wireshark, or Little Snitch
- Practice defensive detections (EDR / IDS)
- Build detections and alerts in SOC simulations

> ⚠️ **NOTE:** This script has only been tested on **macOS**. It has not been tested on Linux or Windows systems.

---

## 🛠️ Requirements

- Python 3.x  
- macOS environment (for clipboard functionality)  
- A C2 listener (e.g., `nc -lvnp 4444` on a Kali VM)  
- Proper firewall/network permissions in lab setup

---

## 🚀 Usage (Lab Environment)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rat-education-wardog.git
   cd rat-education-wardog
   ```

2. **Edit `rat.py`**
   - Change the `HOST` variable to your Kali or lab VM IP.
   - Set the `PORT` variable to your chosen listener port.

3. **Start your C2 listener on Kali**
   ```bash
   nc -lvnp 4444
   ```

4. **Run the RAT on macOS (for testing)**
   ```bash
   python3 rat.py
   ```

5. **Embed into macOS app package (optional)**  
   Place the `rat.py` inside your phishing app bundle (`YourApp.app/Contents/MacOS/`) so it runs alongside the app for demonstration.

---

## 🧪 Detection & Monitoring

For defenders and blue teamers, you can use **Suricata** or similar tools to detect RAT traffic:

**Quick Suricata Install (Linux):**
```bash
sudo apt update
sudo apt install suricata -y
sudo systemctl enable suricata
sudo systemctl start suricata
```

Monitor traffic to the defined `HOST:PORT` to see the RAT behavior in real time.

---

## ⚖️ Legal Disclaimer

This repository is for **authorized security testing, research, and education** only.  
Using this code on networks or systems without **explicit permission** is illegal.  
The authors and contributors are **not responsible** for any misuse or damages caused.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project for educational and research purposes with proper attribution.

---

## 🧠 Author / Project

- 🐺 **Wardog Security** — Focused on practical, offensive security education.  
- 💻 Ideal for Red Team & Blue Team labs



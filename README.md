# 🛡️ Python Log Analyzer

A Python-based log analysis tool that detects suspicious login activity by parsing system logs and identifying repeated failed login attempts from IP addresses.

---

## 📌 Project Purpose

This project simulates how security analysts monitor logs to detect potential brute-force attacks or unauthorized access attempts.

It reads log files, extracts important data, and generates a security report.

---

## ⚙️ Features

✔ Extracts IP addresses from logs  
✔ Detects failed login attempts  
✔ Counts failures per IP  
✔ Generates a summary report  
✔ Uses regex for pattern detection  

---

## 🧠 Concepts Used

- Python File Handling  
- Regular Expressions (`re`)  
- Dictionaries & Loops  
- Modular Programming  
- Basic Security Log Analysis  

---

## 📂 Project Structure
```
log_analyzer/
│
├── main.py       # Runs the program
├── analyzer.py   # Log parsing logic
├── utils.py      # Helper functions
├── log.txt       # Sample log file
├── report.txt    # Generated report

---

## ▶️ How to Run

```bash
python main.py

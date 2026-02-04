"""
Python Log Analyzer
Analyzes log files to detect failed login attempts and suspicious IPs.
"""

import analyzer

logs = analyzer.read_logs("log.txt")
ip_fail_count = analyzer.count_failed_logins(logs)
suspicious_ips = analyzer.get_suspicious_ips(ip_fail_count)

print("Failed Login Attempts Per IP:\n")

for ip, count in ip_fail_count.items():
    print(ip, "→", count, "failures")

print("\nSuspicious IPs:")
for ip in suspicious_ips:
    print(ip, "⚠️ Possible brute-force activity")

with open("report.txt", "w", encoding="utf-8") as report:
    report.write("Log Analysis Report\n")
    report.write("===================\n\n")

    for ip, count in ip_fail_count.items():
        report.write(f"{ip} -> {count} failures\n")

    report.write("\nSuspicious IPs:\n")
    for ip in suspicious_ips:
        report.write(f"{ip}\n")


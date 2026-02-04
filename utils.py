import re

def extract_ip(line):
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    if match:
        return match.group()
    return None


def is_failed_login(line):
    return "Failed login" in line


def extract_user(line):
    match = re.search(r"user=(\w+)", line)
    if match:
        return match.group(1)
    return None

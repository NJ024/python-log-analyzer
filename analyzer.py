import utils

def read_logs(filename):
    with open(filename, "r") as file:
        return file.readlines()


def count_failed_logins(logs):
    ip_fail_count = {}

    for line in logs:
        if utils.is_failed_login(line):
            ip = utils.extract_ip(line)

            if ip:
                if ip in ip_fail_count:
                    ip_fail_count[ip] += 1
                else:
                    ip_fail_count[ip] = 1

    return ip_fail_count


def get_suspicious_ips(ip_fail_count, threshold=2):
    suspicious = []

    for ip, count in ip_fail_count.items():
        if count >= threshold:
            suspicious.append(ip)

    return suspicious

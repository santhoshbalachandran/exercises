import os, sys
from collections import Counter

def read_file(file):
    try:
        with open(file) as f:
            for line in f:
                yield line.strip()
    except Exception as e:
        print(f"[Error]: Failed to open the file - {e}")
        sys.exit(1)

def analyse_log(log_file: str) -> dict:
    stats = Counter({"ERROR": 0, "WARNING": 0, "INFO": 0})
    for line in read_file(log_file):
        parts = line.split(" - ")
        if len(parts) > 1:
            level = parts[1].strip().upper()
            if level in stats:
                stats[level] += 1
    return stats


if __name__ == "__main__":
    log_file = input("Enter a log file: ")

    if not os.path.exists(log_file):
        print(f"[Error]: '{log_file}' file not found.")
        sys.exit(1)    

    stats = analyse_log(log_file)

    for key, value in stats.items():
        print(f'{key}: {value}')
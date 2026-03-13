def count_log_levels(logs):
    counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}

    for line in logs:
        level = line.split(":")[0]    
        if level in counts:
            counts[level] += 1

    return counts


logs = ["ERROR: disk full", "INFO: started", "ERROR: timeout", "WARN: low memory"]
print(count_log_levels(logs))
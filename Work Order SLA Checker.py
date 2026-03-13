def get_sla_hours(priority):
    sla_hours={
        "p1": 4,
        "p2": 8,
        "p3": 24,
        "p4": 72,
    }
    return -1 if priority not in range(1,5) else sla_hours[f"p{priority}"]
# Expected outputs

print(get_sla_hours(1)) # → 4​

print(get_sla_hours(2)) # → 8​

print(get_sla_hours(3)) # → 24​

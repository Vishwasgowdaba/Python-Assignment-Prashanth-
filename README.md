## Code Insights

This assignment contains two simple Python utility functions.

The first function, `count_log_levels(logs)`, processes a list of log messages and counts how many times each log level (INFO, WARN, ERROR) appears. 
It initializes a dictionary with these log levels set to zero and then iterates through each log entry. For every log message, it extracts the log level by splitting the string at the colon (`:`).
If the extracted level exists in the dictionary, the corresponding count is incremented. After processing all log messages, 
the function returns the dictionary with the final counts. This approach makes it easy to analyze log severity distribution.

The second function, `get_sla_hours(priority)`, determines the SLA resolution time based on a ticket's priority level. A dictionary maps priorities P1 to P4 to their respective SLA hours (4, 8, 24, and 72). 
The function first checks whether the given priority is within the valid range of 1 to 4. If it is valid, it dynamically constructs the key (e.g., `"p1"`, `"p2"`) and retrieves the corresponding SLA value from the dictionary.
If the priority is invalid, the function returns `-1`. This design keeps the logic simple, readable, and easy to update if SLA values change.


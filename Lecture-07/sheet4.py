performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95], 
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    }, 
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73], 
        "Ivan": [60, 62, 64, 66]
    }
}

average_scores = {}
for department, employees in performance_data.items():
    average_scores[department] = {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores[department][employee] = average

print(f"Average Performance Scores: ", average_scores)

top_performers = {}
for department, employees in average_scores.items():
    top_employee = ""
    top_avg = -1
    for employee, avg in employees.items():
        if avg > top_avg:
            top_avg = avg
            top_employee = employee
    top_performers[department] = {
        top_employee,
        top_avg
    }

print(f"Top Performers: ", top_performers)
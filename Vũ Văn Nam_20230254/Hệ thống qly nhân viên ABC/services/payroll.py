def total_salary(employees):
    return sum(e.calculate_salary() for e in employees)

def top_3_salary(employees):
    return sorted(employees, key=lambda e: e.calculate_salary(), reverse=True)[:3]

def count_by_type(employees):
    result = {}
    for e in employees:
        t = e.__class__.__name__
        result[t] = result.get(t, 0) + 1
    return result

def avg_projects(employees):
    if not employees:
        return 0
    return sum(len(e.projects) for e in employees) / len(employees)
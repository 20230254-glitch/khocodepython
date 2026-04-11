def total_salary(employees):
    if not employees:
        return 0

    return sum(e.calculate_salary() for e in employees)


def top_3_salary(employees):
    if not employees:
        return []

    return sorted(
        employees,
        key=lambda e: e.calculate_salary(),
        reverse=True
    )[:3]


def count_by_type(employees):
    result = {
        "Manager": 0,
        "Developer": 0,
        "Intern": 0
    }

    for e in employees:
        t = e.__class__.__name__
        if t in result:
            result[t] += 1
        else:
            result[t] = 1  # phòng trường hợp thêm loại mới

    return result


def avg_projects(employees):
    if not employees:
        return 0

    total_projects = 0

    for e in employees:
      
        total_projects += len(getattr(e, "projects", []))

    return total_projects / len(employees)
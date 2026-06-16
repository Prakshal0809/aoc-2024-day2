def is_safe(levels):
    increasing = True
    decreasing = True

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if not (1 <= diff <= 3):
            increasing = False
        if not (-3 <= diff <= -1):
            decreasing = False

    return increasing or decreasing


def count_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def parse_input(filename):
    reports = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                numbers = [int(x) for x in line.split()]
                reports.append(numbers)
    return reports


reports = parse_input("input.txt")
print("Number of safe reports:", count_safe_reports(reports))
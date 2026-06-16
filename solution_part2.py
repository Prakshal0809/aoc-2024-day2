# Brute force approach
# So my first thought was just to follow the rule directly. A report is safe if it's already safe, 
# or if removing one level makes it safe, so I figured I'd literally do that. 
# First I check if the report is already safe as it is, and if it is, I'm done. 
# If it's not, then I go through each level one by one, remove that level, and check again. 
# If removing any single level makes it safe, I return true; if I've tried removing every position and none of them work, then it's actually unsafe.
# I knew this approach is O(n²), since for each report I'm doing up to n+1 checks and each one scans the whole list, 
# but the reports are short so the cost is basically nothing, and the logic is simple and obviously correct.

# Optimal O(n) approach: only check removals near the first break point

def safe_no_removal(levels):
    up = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    down = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return up or down


def is_safe_with_dampener(levels):
    n = len(levels)
    if n <= 2:
        return True

    if safe_no_removal(levels):
        return True

    candidates = set()
    for sign in (1, -1):
        for i in range(n - 1):
            diff = (levels[i + 1] - levels[i]) * sign
            if not (1 <= diff <= 3):
                if i - 1 >= 0:
                    candidates.add(i - 1)
                candidates.add(i)
                candidates.add(i + 1)
                break

    for j in candidates:
        if safe_no_removal(levels[:j] + levels[j + 1:]):
            return True

    return False


def count_safe(reports):
    count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            count += 1
    return count


def parse_input(filename):
    reports = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                reports.append([int(x) for x in line.split()])
    return reports


def main():
    reports = parse_input("input.txt")
    print("Part 2 - Safe reports with dampener:", count_safe(reports))


if __name__ == "__main__":
    main()
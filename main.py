# Here's a Python implementation of Zeller's Congruence
def get(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    d = (h + 5) % 7
    match d:
        case 0: return "Saturday"
        case 1: return"Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"

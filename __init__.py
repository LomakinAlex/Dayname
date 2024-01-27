def dayname(day:int, month:int, year:int) -> str:
    if month < 3:
        month += 12
        year -= 1
    K:int = year % 100
    J:int = year // 100
    h:int = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    d:int = (h + 5) % 7
    return ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")[d]

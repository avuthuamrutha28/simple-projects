#work hours by day
def get_work_hours(day):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = [
        [3, 3, 3, 3, 3, 3, 0],
        [2, 2, 2, 2, 2, 1, 0],
        [2, 2, 2, 1, 1, 0, 0]
    ]
    idx = days.index(day)
    return [row[idx] for row in hours]

print("Thu:", get_work_hours("Thu"))
print("Sat:", get_work_hours("Sat"))

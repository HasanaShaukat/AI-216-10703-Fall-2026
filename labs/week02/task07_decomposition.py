# Problem:
# Analyze student attendance and classify students as eligible or below the attendance requirement.

# Inputs:
attendance = [82, 74.9, 75, 91, 60, 88, 70]

# Rules:
# Attendance of 75 or above is eligible.
# Attendance below 75 is not eligible.

# Repetition:
eligible_count = 0
below_count = 0

for value in attendance:
    if value >= 75:
        eligible_count += 1
    else:
        below_count += 1

# Outputs:
total_students = len(attendance)

if total_students > 0:
    eligible_percentage = (eligible_count / total_students) * 100
else:
    eligible_percentage = 0

print("Eligible students:", eligible_count)
print("Below requirement:", below_count)
print("Eligible percentage:", format(eligible_percentage, ".2f"), "%")
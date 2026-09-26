scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

meeting_target = 0
below_target = 0

for score in scores:
    if score >= threshold:
        meeting_target += 1
    else:
        below_target += 1

if len(scores) > 0:
    average_score = sum(scores) / len(scores)
    percentage_meeting = (meeting_target / len(scores)) * 100
else:
    average_score = 0
    percentage_meeting = 0

print("Scores meeting target:", meeting_target)
print("Scores below target:", below_target)
print("Average score:", format(average_score, ".2f"))
print("Percentage meeting target:", format(percentage_meeting, ".2f"), "%")

# A reusable function can be used later to analyze different score lists without repeating the same code.
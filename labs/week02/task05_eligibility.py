age = 19
programming_score = 72
prerequisite_completed = True

eligible = True

if age < 18:
    eligible = False

if programming_score < 60:
    eligible = False

if not prerequisite_completed:
    eligible = False

if eligible:
    print("Eligible")
else:
    print("Not eligible")

    if age < 18:
        print("Requirement not met: Age must be 18 or above")

    if programming_score < 60:
        print("Requirement not met: Programming score must be 60 or above")

    if not prerequisite_completed:
        print("Requirement not met: Prerequisite must be completed")
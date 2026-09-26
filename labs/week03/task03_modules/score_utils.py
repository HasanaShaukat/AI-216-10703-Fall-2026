def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)


def is_passing(score, passing_score=50):
    return score >= passing_score


def count_above_threshold(scores, threshold):
    count = 0

    for score in scores:
        if score >= threshold:
            count += 1

    return count


if __name__ == "__main__":
    scores = [72, 88, 45, 91, 67]

    print("Demo Average:", calculate_average(scores))
    print("Demo Passing:", is_passing(scores[0]))
    print("Demo Above 80:", count_above_threshold(scores, 80))
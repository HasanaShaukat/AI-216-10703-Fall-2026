class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for score in self.scores if score >= threshold)

    def highest(self):
        if not self.scores:
            return None
        return max(self.scores)

    def lowest(self):
        if not self.scores:
            return None
        return min(self.scores)
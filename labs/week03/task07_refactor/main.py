from preprocessing import clean_scores
from analyzer import ScoreAnalyzer


raw_scores = [78, -5, 92, 110, 67, 88]

cleaned_scores = clean_scores(raw_scores)

analyzer = ScoreAnalyzer(cleaned_scores)

print("Raw Data:", raw_scores)
print("Clean Data:", cleaned_scores)
print("Average:", analyzer.average())
print("Qualified:", analyzer.count_above(70))
print("Highest:", analyzer.highest())
print("Lowest:", analyzer.lowest())
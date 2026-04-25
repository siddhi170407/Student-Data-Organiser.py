import numpy as np

class Analyzer:
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = np.array(scores, dtype=float)

    def calculate_overall_average(self):
        return round(float(np.mean(self.scores)), 2)

    def calculate_subject_average(self, all_scores):
        arr = np.array(all_scores, dtype=float)
        return np.mean(arr, axis=0).tolist()

    def find_weak_subjects(self):
        return [self.subjects[i] for i, s in enumerate(self.scores) if s < 60]

    def find_strong_subjects(self):
        return [self.subjects[i] for i, s in enumerate(self.scores) if s >= 80]

    def get_highest_subject(self):
        return self.subjects[int(np.argmax(self.scores))]

    def get_lowest_subject(self):
        return self.subjects[int(np.argmin(self.scores))]

    def get_full_report(self):
        return {
            "average": self.calculate_overall_average(),
            "highest_subject": self.get_highest_subject(),
            "lowest_subject": self.get_lowest_subject(),
            "weak_subjects": self.find_weak_subjects(),
            "strong_subjects": self.find_strong_subjects()
        }

import random

class InsightEngine:
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = scores

        self.quotes = [
            "Consistency beats motivation.",
            "Success is the sum of small efforts repeated daily.",
            "Push yourself, because no one else will do it for you.",
            "Don’t watch the clock; do what it does. Keep going.",
            "Small progress is still progress.",
            "Dream big. Work hard. Stay focused."
        ]

    # 🔹 Generate all subject suggestions
    def generate_suggestions(self):
        suggestions = []

        for subject, score in zip(self.subjects, self.scores):
            feedback = self.get_subject_feedback(subject, score)
            suggestions.append(feedback)

        return suggestions

    # 🔹 Feedback for a single subject
    def get_subject_feedback(self, subject, score):
        if score < 50:
            return f"{subject}: Needs serious attention. Practice daily and clear basics."

        elif 50 <= score < 65:
            return f"{subject}: Needs improvement. Revise concepts and solve more problems."

        elif 65 <= score < 80:
            return f"{subject}: Average. Keep practicing and focus on weak areas."

        else:  # 80+
            return f"{subject}: Strong subject! Try advanced questions to improve further."

    # 🔹 Get random motivational quote
    def get_daily_quote(self):
        return random.choice(self.quotes)
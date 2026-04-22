class Student:
    def __init__(self, roll_no, name, subjects, marks_history=None):
        self.roll_no = str(roll_no)
        self.name = name
        self.subjects = subjects
        self.marks_history = marks_history if marks_history is not None else []

    def add_test_record(self, date, scores):
        record = {
            "date": date,
            "scores": scores
        }
        self.marks_history.append(record)

    def get_latest_marks(self):
        if not self.marks_history:
            return None
        return self.marks_history[-1]

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "subjects": self.subjects,
            "marks_history": self.marks_history
        }
import json
import os
from student import Student


class DataManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {"students": []}

        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {"students": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_student(self, student):
        # Check duplicate roll number
        for existing_student in self.data["students"]:
            if existing_student["roll_no"] == student.roll_no:
                return False, "Student with this roll number already exists."

        self.data["students"].append(student.to_dict())
        self.save_data()
        return True, "Student added successfully."

    def get_student(self, roll_no):
        roll_no = str(roll_no)
        for student in self.data["students"]:
            if student["roll_no"] == roll_no:
                return student
        return None

    def update_student(self, roll_no, new_name=None, new_subjects=None, new_marks_history=None):
        roll_no = str(roll_no)
        for student in self.data["students"]:
            if student["roll_no"] == roll_no:
                if new_name is not None:
                    student["name"] = new_name
                if new_subjects is not None:
                    student["subjects"] = new_subjects
                if new_marks_history is not None:
                    student["marks_history"] = new_marks_history

                self.save_data()
                return True, "Student updated successfully."

        return False, "Student not found."

    def delete_student(self, roll_no):
        roll_no = str(roll_no)
        for i, student in enumerate(self.data["students"]):
            if student["roll_no"] == roll_no:
                del self.data["students"][i]
                self.save_data()
                return True, "Student deleted successfully."

        return False, "Student not found."

    def add_marks_record(self, roll_no, date, scores):
        roll_no = str(roll_no)
        for student in self.data["students"]:
            if student["roll_no"] == roll_no:
                record = {
                    "date": date,
                    "scores": scores
                }
                student["marks_history"].append(record)
                self.save_data()
                return True, "Marks record added successfully."

        return False, "Student not found."

    def get_all_students(self):
        return self.data["students"]
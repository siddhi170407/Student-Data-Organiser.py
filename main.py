from student import Student
from data_manager import DataManager
from analysis import Analyzer
from insights import InsightEngine
from visualizer import Visualizer


class MainApp:
    def __init__(self):
        self.data_manager = DataManager()
        self.visualizer = Visualizer()

    def show_menu(self):
        print("\n===== Student Data Organizer =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. Analyze Performance")
        print("4. Show Graph")
        print("5. Daily Motivation")
        print("6. Update Student")
        print("7. Delete Student")
        print("8. Exit")

    def add_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Student Name: ")

        existing_student = self.data_manager.get_student(roll_no)
        if existing_student:
            print("Student with this roll number already exists.")
            return

        subjects = []
        scores = []

        try:
            count = int(input("Enter number of subjects: "))
            for i in range(count):
                subject = input(f"Enter subject {i + 1} name: ")
                mark = float(input(f"Enter marks for {subject}: "))

                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100.")
                    return

                subjects.append(subject)
                scores.append(mark)

            date = input("Enter test date (YYYY-MM-DD): ")

            student = Student(roll_no, name, subjects)
            student.add_test_record(date, scores)

            success, message = self.data_manager.add_student(student)
            print(message)

        except ValueError:
            print("Invalid input. Please enter numbers correctly.")

    def view_student(self):
        roll_no = input("Enter Roll No: ")
        student = self.data_manager.get_student(roll_no)

        if not student:
            print("Student not found.")
            return

        print("\n----- Student Record -----")
        print(f"Name: {student['name']}")
        print(f"Roll No: {student['roll_no']}")

        if not student["marks_history"]:
            print("No marks available.")
            return

        latest_record = student["marks_history"][-1]
        print(f"Date: {latest_record['date']}")

        print("\nSubjects and Marks:")
        for subject, score in zip(student["subjects"], latest_record["scores"]):
            print(f"{subject}: {score}")

    def analyze_performance(self):
        roll_no = input("Enter Roll No: ")
        student = self.data_manager.get_student(roll_no)

        if not student:
            print("Student not found.")
            return

        if not student["marks_history"]:
            print("No marks available for analysis.")
            return

        subjects = student["subjects"]
        scores = student["marks_history"][-1]["scores"]

        analyzer = Analyzer(subjects, scores)
        report = analyzer.get_full_report()

        insight_engine = InsightEngine(subjects, scores)
        suggestions = insight_engine.generate_suggestions()

        print("\n----- Performance Report -----")
        print(f"Name: {student['name']}")
        print(f"Roll No: {student['roll_no']}")
        print(f"Average Marks: {report['average']}")
        print(f"Highest Subject: {report['highest_subject']}")
        print(f"Lowest Subject: {report['lowest_subject']}")
        print(f"Weak Subjects: {report['weak_subjects']}")
        print(f"Strong Subjects: {report['strong_subjects']}")

        print("\n----- Suggestions -----")
        for suggestion in suggestions:
            print("-", suggestion)

    def show_graph(self):
        roll_no = input("Enter Roll No: ")
        student = self.data_manager.get_student(roll_no)

        if not student:
            print("Student not found.")
            return

        if not student["marks_history"]:
            print("No marks available for graph.")
            return

        subjects = student["subjects"]
        latest_scores = student["marks_history"][-1]["scores"]

        self.visualizer.show_bar_chart(subjects, latest_scores)

        if len(student["marks_history"]) > 1:
            dates = []
            averages = []

            for record in student["marks_history"]:
                dates.append(record["date"])
                avg = sum(record["scores"]) / len(record["scores"])
                averages.append(avg)

            self.visualizer.show_progress_chart(dates, averages)
        else:
            print("Only one test record available. Progress chart needs at least two records.")

    def daily_motivation(self):
        insight_engine = InsightEngine([], [])
        quote = insight_engine.get_daily_quote()

        print("\n----- Daily Motivation -----")
        print(quote)

    def update_student(self):
        roll_no = input("Enter Roll No to update: ")
        student = self.data_manager.get_student(roll_no)

        if not student:
            print("Student not found.")
            return

        print("1. Update Name")
        print("2. Add New Marks Record")

        choice = input("Enter choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")
            success, message = self.data_manager.update_student(
                roll_no,
                new_name=new_name
            )
            print(message)

        elif choice == "2":
            try:
                scores = []
                for subject in student["subjects"]:
                    mark = float(input(f"Enter marks for {subject}: "))

                    if mark < 0 or mark > 100:
                        print("Marks should be between 0 and 100.")
                        return

                    scores.append(mark)

                date = input("Enter test date (YYYY-MM-DD): ")

                success, message = self.data_manager.add_marks_record(
                    roll_no,
                    date,
                    scores
                )
                print(message)

            except ValueError:
                print("Invalid marks entered.")

        else:
            print("Invalid choice.")

    def delete_student(self):
        roll_no = input("Enter Roll No to delete: ")

        confirm = input("Are you sure you want to delete this student? (yes/no): ")

        if confirm.lower() == "yes":
            success, message = self.data_manager.delete_student(roll_no)
            print(message)
        else:
            print("Delete cancelled.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_student()

            elif choice == "3":
                self.analyze_performance()

            elif choice == "4":
                self.show_graph()

            elif choice == "5":
                self.daily_motivation()

            elif choice == "6":
                self.update_student()

            elif choice == "7":
                self.delete_student()

            elif choice == "8":
                print("Thank you for using Student Data Organizer!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = MainApp()
    app.run()

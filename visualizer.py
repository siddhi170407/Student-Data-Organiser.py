import matplotlib.pyplot as plt


class Visualizer:
    def show_bar_chart(self, subjects, scores):
        plt.figure()
        plt.bar(subjects, scores)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Subject-wise Marks")
        plt.ylim(0, 100)
        plt.show()

    def show_progress_chart(self, dates, averages):
        plt.figure()
        plt.plot(dates, averages, marker="o")
        plt.xlabel("Test Dates")
        plt.ylabel("Average Marks")
        plt.title("Progress Over Time")
        plt.ylim(0, 100)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

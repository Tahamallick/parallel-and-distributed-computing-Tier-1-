import pandas as pd
import time


def load_students_data(file_path):
    return pd.read_csv(file_path)


def load_fees_data(file_path):
    return pd.read_csv(file_path)


# Linear Implementation
def find_students_with_late_fees_unoptimized(students_data, fees_data):
    start_time = time.time()

    late_fees_students = []
    for _, fee in fees_data.iterrows():
        if fee["Paid_Status"] == "Late":
            student_id = fee["Student_ID"]
            student = students_data[students_data["Student_ID"] == student_id]  # Get student information
            if not student.empty:
                student_info = student.iloc[0]
                late_fees_students.append({
                    "Student_ID": student_info["Student_ID"],
                    "Name": student_info["Name"],
                    "Class": student_info["Class"],
                    "Fee_Amount": fee["Fee_Amount"]
                })

    end_time = time.time()
    print(f"Linear Execution Time: {end_time - start_time:.2f} seconds")
    return late_fees_students


# Main Function
if __name__ == "__main__":
    students_data = load_students_data('data/students.csv')
    fees_data = load_fees_data('data/fees.csv')

    print("Running Linear Implementation...")
    late_students_unoptimized = find_students_with_late_fees_unoptimized(students_data, fees_data)

    print(f"Linear results count: {len(late_students_unoptimized)}")

import pandas as pd
import time
from multiprocessing import Pool, cpu_count
def load_students_data(file_path):
    return pd.read_csv(file_path)

def load_fees_data(file_path):
    return pd.read_csv(file_path)

def process_chunk(chunk, students_data):
    late_fees_students = []
    for _, fee in chunk.iterrows():
        if fee["Paid_Status"] == "Late":
            student_id = fee["Student_ID"]
            student = students_data[students_data["Student_ID"] == student_id]
            if not student.empty:
                student_info = student.iloc[0]
                late_fees_students.append({
                    "Student_ID": student_info["Student_ID"],
                    "Name": student_info["Name"],
                    "Class": student_info["Class"],
                    "Fee_Amount": fee["Fee_Amount"]
                })
    return late_fees_students

# Using multiprocessing For Parallel approach
def find_students_with_late_fees_parallel(students_data, fees_data, num_processes=None):
    start_time = time.time()

    if num_processes is None:
        num_processes = cpu_count()

    chunk_size = len(fees_data) // num_processes
    chunks = [fees_data.iloc[i:i + chunk_size] for i in range(0, len(fees_data), chunk_size)]

    # processing chunks in parallel
    with Pool(num_processes) as pool:
        late_fees_students = pool.starmap(process_chunk, [(chunk, students_data) for chunk in chunks])

    late_fees_students = [item for sublist in late_fees_students for item in sublist]

    end_time = time.time()
    print(f"Parallel Execution Time (Multiprocessing): {end_time - start_time:.2f} seconds")
    return late_fees_students

# Main Function
if __name__ == "__main__":
    students_data = load_students_data('data/students.csv')
    fees_data = load_fees_data('data/fees.csv')
    print("Running Parallel Implementation using Multiprocessing...")
    late_students_parallel = find_students_with_late_fees_parallel(students_data, fees_data, num_processes=cpu_count())
    print(f"Parallel results count: {len(late_students_parallel)}")

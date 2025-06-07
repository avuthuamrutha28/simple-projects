import pandas as pd

# Load data
df = pd.read_csv("coursedata.csv")

def get_students_by_qualification():
    q = input("Enter qualification (e.g., BE, BSc, BCom): ")
    print(df[df["Qualification"].str.upper() == q.upper()])

def count_students_by_qualification():
    print(df["Qualification"].value_counts())

def count_placed_students():
    print("Placed students count:", (df["Placed"] == "Y").sum())

def count_completed_not_placed():
    completed = df["Course Completed"] == "Y"
    not_placed = df["Placed"] == "N"
    print("Completed but not placed:", df[completed & not_placed].shape[0])

def count_placed_and_not_placed():
    print(df["Placed"].value_counts())

def search_student_by_name():
    name = input("Enter name to search: ")
    print(df[df["Name"].str.contains(name, case=False)])

def avg_success_rate_batch():
    batch = input("Enter batch name: ")
    batch_df = df[df["Batch"] == batch]
    if not batch_df.empty:
        placed = (batch_df["Placed"] == "Y").sum()
        rate = (placed / len(batch_df)) * 100
        print(f"Success rate of {batch}: {rate:.2f}%")
    else:
        print("No such batch found.")

def max_percentage_student():
    max_score = df["Score"].max()
    print(df[df["Score"] == max_score])

def get_all_student_names():
    print(df["Name"].tolist())

def get_name_qualification_score():
    print(df[["Name", "Qualification", "Score"]])

def menu():
    while True:
        print("\n----- COURSE DATA ANALYSIS MENU -----")
        print("1. Get all students by qualification")
        print("2. Get count of all students by qualification")
        print("3. Get count of students who got placed")
        print("4. Get count of students who completed course but not placed")
        print("5. Get count of placed and not placed students")
        print("6. Search student by name")
        print("7. Get average success rate of a batch")
        print("8. Get max percentage scored student details")
        print("9. Get all student names")
        print("10. Get all student name, qualification, score")
        print("0. Exit")

        choice = input("Enter your choice (0-10): ")

        if choice == '1':
            get_students_by_qualification()
        elif choice == '2':
            count_students_by_qualification()
        elif choice == '3':
            count_placed_students()
        elif choice == '4':
            count_completed_not_placed()
        elif choice == '5':
            count_placed_and_not_placed()
        elif choice == '6':
            search_student_by_name()
        elif choice == '7':
            avg_success_rate_batch()
        elif choice == '8':
            max_percentage_student()
        elif choice == '9':
            get_all_student_names()
        elif choice == '10':
            get_name_qualification_score()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


menu()

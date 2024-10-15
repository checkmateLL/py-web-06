import sqlite3
from datetime import datetime
from faker import Faker
from random import randint, choice

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20  # Up to 20 grades per student

def generate_fake_data():
    fake = Faker()

    groups = [fake.unique.word() for _ in range(NUMBER_GROUPS)]
    students = [fake.unique.name() for _ in range(NUMBER_STUDENTS)]
    teachers = [fake.unique.name() for _ in range(NUMBER_TEACHERS)]
    subjects = [fake.unique.word() for _ in range(NUMBER_SUBJECTS)]

    return groups, students, teachers, subjects

def insert_data_to_db(groups, students, teachers, subjects):
    with sqlite3.connect('db_lite.sqlite') as conn:
        cursor = conn.cursor()

        # Insert groups
        cursor.executemany("INSERT INTO groups (group_name) VALUES (?)", [(g,) for g in groups])

        # Insert teachers
        cursor.executemany("INSERT INTO teachers (teacher_name) VALUES (?)", [(t,) for t in teachers])

        # Insert subjects
        for subject in subjects:
            cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)",
                           (subject, randint(1, NUMBER_TEACHERS)))

        # Insert students
        for student in students:
            cursor.execute("INSERT INTO students (student_name, group_id) VALUES (?, ?)",
                           (student, randint(1, NUMBER_GROUPS)))

        # Insert grades
        fake = Faker()
        for student_id in range(1, NUMBER_STUDENTS + 1):
            for _ in range(NUMBER_GRADES):
                subject_id = randint(1, NUMBER_SUBJECTS)
                grade = randint(1, 100)  # Changed to 1-100 to match the CHECK constraint
                grade_date = fake.date_between(start_date='-1y', end_date='today')
                cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                               (student_id, subject_id, grade, grade_date))

        conn.commit()

def main():
    groups, students, teachers, subjects = generate_fake_data()
    insert_data_to_db(groups, students, teachers, subjects)
    print("Database has been populated with fake data.")

if __name__ == "__main__":
    main()
"""Python equivalent of Java admin "View All Students" feature.

Usage:
  python enrollment.py

The program uses seeded sample data and supports a minimal admin
interface (login with password "admin123").
"""

from dataclasses import dataclass, field
from typing import Dict, List

ADMIN_PASSWORD = "admin123"
SEPARATOR = "=" * 70
THIN_SEP = "-" * 70


@dataclass
class Student:
    id: str
    name: str
    major: str
    enrolled_courses: List[str] = field(default_factory=list)

    def is_enrolled_in(self, course_code: str) -> bool:
        return course_code in self.enrolled_courses

    def __str__(self) -> str:
        enrolled = ", ".join(self.enrolled_courses) if self.enrolled_courses else "None"
        return f"{self.id:<12} {self.name:<25} {self.major:<20} {enrolled}"


class EnrollmentSystem:
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, student: Student) -> bool:
        if student is None or student.id in self.students:
            return False
        self.students[student.id] = student
        return True

    def get_student(self, student_id: str):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    def seed_default_data(self):
        # Mimic Java DataManager default student accounts.
        self.add_student(Student("STU001", "Alice Johnson", "Computer Science", ["CS101"]))
        self.add_student(Student("STU002", "Bob Smith", "Mathematics", []))
        self.add_student(Student("STU003", "Carol Williams", "Information Technology", ["CS201"]))


def admin_view_students(system: EnrollmentSystem):
    print("\n" + SEPARATOR)
    print("  ALL STUDENTS")
    print(SEPARATOR)
    students = system.get_all_students()

    if not students:
        print("  No students registered.")
        return

    print(f"  {'ID':<15} {'Name':<25} {'Major':<20} Enrolled Courses")
    print("  " + THIN_SEP)
    for s in students:
        enrolled = ", ".join(s.enrolled_courses) if s.enrolled_courses else "None"
        print(f"  {s.id:<15} {s.name:<25} {s.major:<20} {enrolled}")


def admin_menu(system: EnrollmentSystem):
    while True:
        print("\n" + SEPARATOR)
        print("  ADMIN MENU")
        print(SEPARATOR)
        print("  [1] View All Students")
        print("  [2] Add New Student")
        print("  [3] Exit")
        print(THIN_SEP)
        choice = input("  Select option: ").strip()

        if choice == "1":
            admin_view_students(system)
        elif choice == "2":
            student_id = input("  Student ID: ").strip()
            if not student_id:
                print("  [!] Student ID cannot be empty.")
                continue
            if system.get_student(student_id) is not None:
                print("  [!] Student ID already exists.")
                continue
            name = input("  Full Name: ").strip()
            major = input("  Major: ").strip() or "Undeclared"
            system.add_student(Student(student_id, name, major))
            print("  [✓] Student added.")
        elif choice == "3":
            print("  Goodbye.")
            break
        else:
            print("  [!] Invalid option. Enter 1, 2, or 3.")


def main():
    system = EnrollmentSystem()
    system.seed_default_data()

    print(SEPARATOR)
    print("      COURSE ENROLLMENT SYSTEM (Python)")
    print(SEPARATOR)

    password = input("Enter admin password: ").strip()
    if password != ADMIN_PASSWORD:
        print("[!] Incorrect password.")
        return

    print("Welcome, Administrator!")
    admin_menu(system)


if __name__ == "__main__":
    main()

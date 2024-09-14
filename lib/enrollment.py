from datetime import datetime
from typing import List, Dict, Union

class Enrollment:
    all = []  # Class variable to store all Enrollment instances

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
        Enrollment.all.append(self)  # Track all enrollments

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # List of Enrollment objects
        self._grades = {}  # Dictionary of {Enrollment: grade}

    def add_enrollment(self, enrollment):
        if not isinstance(enrollment, Enrollment):
            raise TypeError("enrollment must be an instance of Enrollment")
        self._enrollments.append(enrollment)
        self._grades[enrollment] = None  # Initialize with no grade

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(grade for grade in self._grades.values() if grade is not None)
        num_courses = len(self._grades)
        if num_courses == 0:
            return 0
        average_grade = total_grades / num_courses
        return average_grade

    def set_grade(self, enrollment, grade):
        if not isinstance(enrollment, Enrollment):
            raise TypeError("enrollment must be an instance of Enrollment")
        if enrollment not in self._grades:
            raise ValueError("Enrollment not found in student's records")
        self._grades[enrollment] = grade

class Course:
    def __init__(self, name):
        self.name = name

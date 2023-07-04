### ()_ 5_PYAPI-78_5_1_task10_VR
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка! Это не студент!'
        else:
            if self.average_grade() > other.average_grade():
                return f'Студент {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Студент {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка! Это не лектор!'
        else:
            if self.average_rate() > other.average_rate():
                return f'Лектор {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Лектор {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'


student_001 = Student('Студик1', 'Студиков1', 'male')
student_001.courses_in_progress += ['Python', 'Git']

student_002 = Student('Студичка2', 'Студикова2', 'female')
student_002.courses_in_progress += ['Python']
student_002.finished_courses += ['Git']

reviewer_001 = Reviewer('Проверялка1', 'Проверялкина1')
reviewer_001.courses_attached += ['Python']

reviewer_002 = Reviewer('Проверяльщик2', 'Проверялкин2')
reviewer_002.courses_attached += ['Git']

lecturer_001 = Lecturer('Лекторина1', 'Лекторникова1')
lecturer_001.courses_attached += ['Python']

lecturer_002 = Lecturer('Лекторин2', 'Лекторников2')
lecturer_002.courses_attached += ['Git']

reviewer_001.rate_hw(student_001, 'Python', 7)
reviewer_002.rate_hw(student_001, 'Git', 6)

reviewer_001.rate_hw(student_002, 'Python', 9)

student_001.rate_lecturer(lecturer_001, 'Python', 8)
student_001.rate_lecturer(lecturer_002, 'Git', 6)

student_002.rate_lecturer(lecturer_001, 'Python', 9)

print(student_001)
print(student_002)
print(reviewer_001)
print(reviewer_002)
print(lecturer_001)
print(lecturer_002)

print(student_001 > student_002)
print(lecturer_001 > lecturer_002)


def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
    all_grades_avg = str(sum(all_grades_list) / len(all_grades_list))
    print(f'Средняя оценка всех студентов за домашние задания по курсу {course}: {all_grades_avg}')


def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = str(sum(all_rates_list) / len(all_rates_list))
    print(f'Средняя оценка всех лекторов в рамках курса {course}: {all_rates_avg}')


avg_grades_all([student_001, student_002], 'Python')
avg_grades_all([student_001, student_002], 'Git')

avg_rates_all([lecturer_001, lecturer_002], 'Python')
avg_rates_all([lecturer_001, lecturer_002], 'Git')
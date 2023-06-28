class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_av(self):
        if self.grades.values():
            sum = 0
            num_of_grades = 0
            for value in self.grades.values():
                num_of_grades += len(value)
                for grade in value:
                    sum += grade
            return round(sum / num_of_grades, 2)
        else:
            return 0

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grade_av()}\
        \nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return info

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in \
        ((self.courses_in_progress or self.finished_courses) and lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка!')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Студента можно сравнить только со Студентом')
        else:
            if self.grade_av() < other.grade_av():
                print(f'У {other.surname} {other.name} средний бал выше')
            elif self.grade_av() == other.grade_av():
                print(f'У {other.surname} {other.name} и {self.surname} {self.name} средний бал одинаков')
            else:
                print(f'У {self.surname} {self.name} средний бал выше')

    def __gt__(self, other):
        if not isinstance(other, Student):
            print(f'Студента можно сравнить только со Студентом')
        else:
            if self.grade_av() > other.grade_av():
                print(f'У {self.surname} {self.name} средний бал выше')
            elif self.grade_av() == other.grade_av():
                print(f'У {other.surname} {other.name} и {self.surname} {self.name} средний бал одинаков')
            else:
                print(f'У {other.surname} {other.name} средний бал выше')

    def __le__(self, other):
        if not isinstance(other, Student):
            print(f'Студента можно сравнить только со Студентом')
        else:
            if self.grade_av() <= other.grade_av():
                if self.grade_av() == other.grade_av():
                    print(f'У {self.surname} {self.name} и {other.surname} {other.name} средний бал одинаков')
                else:
                    print(f'У {other.surname} {other.name} средний бал выше')
            else:
                print(f'У {self.surname} {self.name} средний бал выше')

    def __ge__(self, other):
        if not isinstance(other, Student):
            print(f'Студента можно сравнить только со Студентом')
        else:
            if self.grade_av() >= other.grade_av():
                if self.grade_av() == other.grade_av():
                    print(f'У {self.surname} {self.name} и {other.surname} {other.name} средний бал одинаков')
                else:
                    print(f'У {self.surname} {self.name} средний бал выше')
            else:
                print(f'У {other.surname} {other.name} средний бал выше')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def grade_av(self):
        if self.grades.values():
            sum = 0
            num_of_grades = 0
            for value in self.grades.values():
                num_of_grades += len(value)
                for grade in value:
                    sum += grade
            return round(sum / num_of_grades, 2)
        else:
            return 0

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self.grade_av()}\n'
        return info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Лектора можно сравнить только с Лектором')
        else:
            if self.grade_av() < other.grade_av():
                print(f'У {other.surname} {other.name} средний бал выше')
            elif self.grade_av() == other.grade_av():
                print(f'У {other.surname} {other.name} и {self.surname} {self.name} средний бал одинаков')
            else:
                print(f'У {self.surname} {self.name} средний бал выше')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Лектора можно сравнить только с Лектором')
        else:
            if self.grade_av() > other.grade_av():
                print(f'У {self.surname} {self.name} средний бал выше')
            elif self.grade_av() == other.grade_av():
                print(f'У {other.surname} {other.name} и {self.surname} {self.name} средний бал одинаков')
            else:
                print(f'У {other.surname} {other.name} средний бал выше')

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Лектора можно сравнить только с Лектором')
        else:
            if self.grade_av() <= other.grade_av():
                if self.grade_av() == other.grade_av():
                    print(f'У {self.surname} {self.name} и {other.surname} {other.name} средний бал одинаков')
                else:
                    print(f'У {other.surname} {other.name} средний бал выше')
            else:
                print(f'У {self.surname} {self.name} средний бал выше')

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Лектора можно сравнить только с Лектором')
        else:
            if self.grade_av() >= other.grade_av():
                if self.grade_av() == other.grade_av():
                    print(f'У {self.surname} {self.name} и {other.surname} {other.name} средний бал одинаков')
                else:
                    print(f'У {self.surname} {self.name} средний бал выше')
            else:
                print(f'У {other.surname} {other.name} средний бал выше')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return info

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades.keys():
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Основы языка программирования Python']
lecturer_2 = Lecturer('Алёна', 'Батицкая')
lecturer_2.courses_attached += ['Git - система контроля версий']

student_1 = Student('Евгений', 'Кукарский', 'men')
student_1.courses_in_progress += ['ООП и работа с API']
student_1.finished_courses += ['Основы языка программирования Python'] + ['Git - система контроля версий']
student_1.rate_lecture(lecturer_2, 'Git - система контроля версий', 10)

student_2 = Student('Герман', 'Магер', 'men')
student_2.courses_in_progress += ['ООП и работа с API']
student_2.finished_courses += ['Основы языка программирования Python'] + ['Английский для IT-специалистов']
student_2.rate_lecture(lecturer_1, 'Основы языка программирования Python', 10)

reviewer_1 = Reviewer('Александр', 'Бардин')
reviewer_1.courses_attached += ['ООП и работа с API']
reviewer_1.rate_hw(student_1, 'ООП и работа с API', 10)
reviewer_1.rate_hw(student_2, 'ООП и работа с API', 9)

reviewer_2 = Reviewer('Кирилл', 'Бутылов')
reviewer_2.courses_attached += ['Английский для IT-специалистов']
reviewer_2.rate_hw(student_2, 'Английский для IT-специалистов', 9)


# блок вывода в рамках Задания 3.1
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

# блок сравнений в рамках Задания 3.2
student_1 > student_2
student_1 < student_2
student_1 >= student_2
student_1 <= student_2

lecturer_1 > lecturer_2
lecturer_1 < lecturer_2
lecturer_1 >= lecturer_2
lecturer_1 <= lecturer_2

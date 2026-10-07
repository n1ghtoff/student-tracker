#Учет студентов
students = [
    "Нурлыхан",
    "Рақымжан",
    "Ерсары",
    "Серікқали"
]


def show_students():
    print("Список студентов:")
    for student in students:
        print(student)


def search_student(name):
    for student in students:
        if student.lower() == name.lower():
            print(f"Студент найден: {student}")
            return

    print("Студент не найден")


def add_student(name):
    students.append(name)
    print(f"Студент добавлен: {name}")


show_students()
search_student("Нурлыхан")
add_student("Айдос")
show_students()


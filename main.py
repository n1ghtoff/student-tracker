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


show_students()
def search_student(name):
    for student in students:
        if student.lower() == name.lower():
            print(f"Студент найден: {student}")
            return

    print("Студент не найден")

    search_student("Нурлыхан")

    def add_student(name):
    students.append(name)
    print(f"Студент добавлен: {name}");

add_student("Айдос");
show_students();
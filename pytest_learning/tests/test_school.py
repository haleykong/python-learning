import pytest

# Custom Exceptions and Classes
from source.school import Classroom, Teacher, Student, TooManyStudents

# Fixtures for test setup
@pytest.fixture
def default_classroom():
    teacher = Teacher("Minerva McGonagall")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
        Student("Neville Longbottom")
    ]
    return Classroom(teacher, students, "Transfiguration")

@pytest.fixture
def full_classroom():
    teacher = Teacher("Severus Snape")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
        Student("Neville Longbottom"),
        Student("Luna Lovegood"),
        Student("Ginny Weasley"),
        Student("Draco Malfoy"),
        Student("Pansy Parkinson"),
        Student("Gregory Goyle"),
        Student("Vincent Crabbe"),
        Student("Theodore Nott")
    ]
    return Classroom(teacher, students, "Potions")

# Test for adding students
def test_add_student_to_classroom(default_classroom):
    new_student = Student("Luna Lovegood")
    default_classroom.add_student(new_student)
    assert new_student in default_classroom.students
    assert len(default_classroom.students) == 5

def test_add_student_to_full_classroom_raises_exception(full_classroom):
    new_student = Student("Luna Lovegood")
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(new_student)

# Test for removing students
@pytest.mark.parametrize("student_name", ["Harry Potter", "Hermione Granger", "Ron Weasley"])
def test_remove_student_from_classroom(default_classroom, student_name):
    default_classroom.remove_student(student_name)
    assert all(student.name != student_name for student in default_classroom.students)

def test_remove_nonexistent_student_from_classroom(default_classroom):
    default_classroom.remove_student("Draco Malfoy")
    assert len(default_classroom.students) == 4

# Test for changing teacher
def test_change_teacher_in_classroom(default_classroom):
    new_teacher = Teacher("Remus Lupin")
    default_classroom.change_teacher(new_teacher)
    assert default_classroom.teacher.name == "Remus Lupin"

# Additional test cases to cover edge cases and additional logic
@pytest.mark.parametrize("new_teacher_name", ["Albus Dumbledore", "Sybill Trelawney"])
def test_change_teacher_with_parametrize(default_classroom, new_teacher_name):
    new_teacher = Teacher(new_teacher_name)
    default_classroom.change_teacher(new_teacher)
    assert default_classroom.teacher.name == new_teacher_name

def test_add_student_then_remove(default_classroom):
    new_student = Student("Luna Lovegood")
    default_classroom.add_student(new_student)
    default_classroom.remove_student("Luna Lovegood")
    assert all(student.name != "Luna Lovegood" for student in default_classroom.students)

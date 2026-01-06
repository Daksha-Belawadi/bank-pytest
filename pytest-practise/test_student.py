from student import student_details


def test_student_details():
    expected_output = (
        "Student ID : 101\n"
        "Student Name : Rahul\n"
        "Student Course : BCA\n"
        "Academic Year : 2024"
    )

    assert student_details(101, "Rahul", "BCA", 2024) == expected_output
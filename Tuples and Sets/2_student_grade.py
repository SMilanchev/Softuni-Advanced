def input_to_list(count):
    return [input() for _ in range(count)]


def grades_counter(values):
    person_grade = {}

    for value in values:
        (name, mark) = value.split(" ")
        if name not in person_grade:
            person_grade[name] = []
        person_grade[name].append(float(mark))

    return person_grade


def avg(marks):
    return sum(marks) / len(marks)


def print_result(person_grade):
    for (name, marks) in person_grade.items():
        avg_mark = avg(marks)
        marks = " ".join(f'{mark:.2f}' for mark in marks)
        print(f"{name} -> {marks} (avg: {avg_mark:.2f})")


print_result(grades_counter(input_to_list(int(input()))))

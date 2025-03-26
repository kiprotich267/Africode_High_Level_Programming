#Arbitrary args/kwargs

# def course_unit(*args):
#     units = []
#     for unit in args:
#         units.append(unit)
#     return units
# course_unit("Html", "Css", "Python", "Database", "Flask")

# def student_info(**info):
#     for key, value in info.items():
#         print(f"{key} : {value}")
# student_info(name="Enock", age=20, course="python")

# def perfomance_report(*args, **kwargs):
#     print(args)
#     print(kwargs)
# perfomance_report({"name":"kirui" , "age":19, "score":90, "grade":"A"}, "Html", "css", "python")

def courses(*args):
    student_courses = []
    for courses in args:
        student_courses.append(courses)
    print(student_courses)
courses("Html", "css", "python", "bootstrap", "Database", "Flask")

def show_student(student_dict):
    print("Student Management System")
    keyword = input("请输入要查询的学生姓名：")
    if keyword in student_dict:
        print(f"查询成功！姓名：{keyword}，成绩：{student_dict[keyword]}")
    else:
        print("未找到该学生信息！")

if __name__ == "__main__":
    # 这里只是临时空字典，后续有录入会往里面添加数据
    student_dict = {}
    show_student(student_dict)
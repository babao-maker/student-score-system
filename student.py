def add_name(student_dict):
    name = input("请输入学生姓名：")
    if name in student_dict:
        print(f"学生【{name}】已存在！")
        return
    # 只新增姓名，成绩预留为空，后续录入成绩功能填充
    student_dict[name] = ""
    print(f"学生【{name}】姓名录入成功，请后续录入成绩！")

if __name__ == "__main__":
    student_dict = {}
    add_name(student_dict)

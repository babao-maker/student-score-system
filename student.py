

def add_name(student_dict):
    name = input("请输入学生姓名：")
    if name in student_dict:
        print(f"学生【{name}】已存在！")
        return
    # 只新增姓名，成绩预留为空，后续录入成绩功能填充
    student_dict[name] = ""
    print(f"学生【{name}】姓名录入成功，请后续录入成绩！")



def add_score(student_dict):
    # 录入学生姓名
    name = input("请输入学生姓名：")
    # 判断学生是否已经存在（已经提前录入姓名）
    if name not in student_dict:
        print(f"错误：不存在学生【{name}】，请先录入该学生姓名！")
        return

    # 录入成绩，转成数字
    try:
        score = float(input("请输入学生成绩："))
    except ValueError:
        print("成绩输入错误，请输入数字！")
        return
    # 更新成绩
    student_dict[name] = score
    print(f"学生【{name}】成绩【{score}】录入成功！")




def show_student(student_dict):
    print("Student Management System")
    keyword = input("请输入要查询的学生姓名：")
    if keyword in student_dict:
        print(f"查询成功！姓名：{keyword}，成绩：{student_dict[keyword]}")
    else:
        print("未找到该学生信息！")

# 修改学生成绩
def modify_score(student_dict):
    name = input("请输入要修改成绩的学生姓名：")
    if name not in student_dict:
        print("未找到该学生！")
        return
    try:
        new_score = float(input("请输入新成绩："))
    except ValueError:
        print("成绩输入错误，请输入数字！")
        return
    student_dict[name] = new_score
    print(f"学生【{name}】成绩修改成功，新成绩：{new_score}")   
if __name__ == "__main__":
    student_dict = {}
    # 再录入成绩
    add_name(student_dict)

    add_score(student_dict)
    show_student(student_dict)
    modify_score(student_dict)

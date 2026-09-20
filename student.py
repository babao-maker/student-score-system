def modify_student(student_list):
    """
    修改学生成绩
    :param student_list: 全局学生列表，每个元素是字典 {"name":xxx, "score":xxx}
    :return: 无返回，直接修改列表里的数据
    """
    name = input("请输入要修改的学生姓名：").strip()
    found = False
    for stu in student_list:
        if stu["name"] == name:
            print(f"找到学生：{name}，原成绩：{stu['score']}")
            try:
                new_score = float(input("请输入新成绩："))
                if 0 <= new_score <= 100:
                    stu["score"] = new_score
                    print("修改成功！")
                else:
                    print("成绩必须在0~100之间，修改失败")
            except ValueError:
                print("输入不是有效数字，修改失败")
            found = True
            break
    if not found:
        print(f"未找到姓名为【{name}】的学生")

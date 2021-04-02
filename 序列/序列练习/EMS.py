#!/usr/bin/python

print(f'{"-" * 10} 欢迎使用员工管理系统 {"-" * 10}')

employees = [['Issac', '19', '男', 'Beijing'], ['Ice', '19', '女', 'Guang Zhou']]

while True:
    print("""
请选择操作：
    1） 查询员工
    2） 添加员工
    3） 删除员工
    4） 退出系统
""")

    operation = input('请选择（1 ~ 4）：')

    print(f'{"-" * 19} >8 {"-" * 19}')

    if operation == '1':
        print('序号\t\t姓名\t\t年龄\t\t性别\t\t住址')

        i = 1
        for employee in employees:
            print(i, end='\t\t')
            for msg in employee:
                print(msg, end='\t\t')
            print('\n', end='')
            i += 1

        print(f'\n{"-" * 19} >8 {"-" * 19}')
    elif operation == '2':
        employee = []

        employee.append(input('请输入姓名：'))
        employee.append(input('请输入年龄：'))
        employee.append(input('请输入性别：'))
        employee.append(input('请输入住址：'))

        print(f'\n{"-" * 19} >8 {"-" * 19}')

        print('姓名\t\t年龄\t\t性别\t\t住址')

        for msg in employee:
            print(msg, end='\t\t')
        print('\n', end='')

        confirm = input('\n确认添加以上员工操作吗 [y/N]：')

        print(f'{"-" * 19} >8 {"-" * 19}')

        if confirm == 'y' or confirm == 'Y':
            employees.append(employee)
            print('操作成功！')
        elif confirm == 'n' or confirm == 'N':
            print('操作已取消！')
        else:
            print('输入有误，操作已取消！')

        print(f'{"-" * 19} >8 {"-" * 19}')
    elif operation == '3':
        if len(employees) != 0:
            while True:
                del_employee_index = int(
                    input(f'请输入要删除的员工序号（1 ~ {len(employees)}）：'))

                print(f'{"-" * 19} >8 {"-" * 19}')

                if del_employee_index > 0 and del_employee_index <= len(
                        employees):
                    break
                else:
                    print('输入有误，请重新输入！')

                    print(f'{"-" * 19} >8 {"-" * 19}')

            print('姓名\t\t年龄\t\t性别\t\t住址')

            for msg in employees[del_employee_index - 1]:
                print(msg, end='\t\t')
            print('\n', end='')

            confirm = input('\n确认删除以上员工的操作吗 [y/N]：')

            print(f'{"-" * 19} >8 {"-" * 19}')

            if confirm == 'y' or confirm == 'Y':
                del employees[del_employee_index - 1]
                print('操作成功！')
            elif confirm == 'n' or confirm == 'N':
                print('操作已取消！')
            else:
                print('输入有误，操作已取消！')

            print(f'{"-" * 19} >8 {"-" * 19}')
        else:
            print('员工数据为空！')

            print(f'{"-" * 19} >8 {"-" * 19}')
    elif operation == '4':
        print('欢迎再次使用！再见！')

        print(f'{"-" * 19} >8 {"-" * 19}')

        break
    else:
        print('输入有误，请重新输入！')

        print(f'{"-" * 19} >8 {"-" * 19}')

input('按回车键退出...')

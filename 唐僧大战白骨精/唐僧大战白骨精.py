#!/usr/bin/python

print(f'{"-" * 10} 唐僧大战白骨精 {"-" * 10}')
print("""
请选择身份：
1） 唐僧
2） 白骨精
""")

identity = input('请选择身份继续游戏🎮（1 / 2）：')

print(f'{"-" * 16} >8 {"-" * 16}')

if identity == '1':
    print('您已经选择 唐僧 作为游戏角色')
elif identity == '2':
    print('你竟然选择了白骨精，太不要脸了，你将以 唐僧 的身份来继续游戏！')
else:
    print('输入有误，自动选择 唐僧 作为游戏角色')

print(f'{"-" * 16} >8 {"-" * 16}')

health_value = 2
aggressivity = 2
boss_health_value = 10
boss_aggressivity = 10

game_over_str = """
  ____    _    __  __ _____    _____     _______ ____  
 / ___|  / \\  |  \\/  | ____|  / _ \\ \\   / / ____|  _ \\ 
| |  _  / _ \\ | |\\/| |  _|   | | | \\ \\ / /|  _| | |_) |
| |_| |/ ___ \\| |  | | |___  | |_| |\\ V / | |___|  _ < 
 \\____/_/   \\_\\_|  |_|_____|  \\___/  \\_/  |_____|_| \\_\\
"""

print(f'唐僧 现在的生命值为 {health_value}, 攻击力为 {aggressivity}')

while True:
    print(f'{"-" * 16} >8 {"-" * 16}')

    print("""请选择接下来的操作：
1） 练级
2） 打 BOSS
3） 逃跑
""")

    action = input('请选择行动继续游戏🎮（1 - 3）：')

    print(f'{"-" * 16} >8 {"-" * 16}')

    if action == '1':
        health_value += 3
        aggressivity += 3
        print(f'唐僧 升级了！生命值为 {health_value}，攻击力为 {aggressivity}！')
    elif action == '2':
        while health_value > 0 and boss_health_value > 0:
            boss_health_value -= aggressivity
            print(f'白骨精 受到了 唐僧 的 {aggressivity} 点伤害！')
            if boss_health_value > 0:
                health_value -= boss_aggressivity
                print(f'唐僧 受到了 白骨精 的 {boss_aggressivity} 点伤害！')

        if health_value <= 0:
            print(f'唐僧 挂了！{game_over_str}')
        else:
            print(f'白骨精 挂了！{game_over_str}')

        break
    elif action == '3':
        print(f'唐僧 一扭头，撒腿就跑！{game_over_str}')
        break
    else:
        print('输入有误，请重新输入！')

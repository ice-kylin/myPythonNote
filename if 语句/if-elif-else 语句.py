age = int(input('请输入你的年龄：'))

if age >= 100:
    print('祝你健康长寿')
elif age >= 60:
    print('你已经退休了')
elif age >= 40:
    print('你已经中年了')
elif age >= 18:
    print('你已经成年了')
else:
    print('你还未成年呢')

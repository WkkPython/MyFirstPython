import random
min_num=1
max_num=100
num =random.randint(min_num,max_num)  # 生成1-100随机数
guess_count = 0  # 初始化猜测次数
while True:
    try:
        guess_count += 1  # 初始值是0，每次循环增加一次计数
        w = int(input("猜猜我是谁！请输入一个1~100数字："))
        if w == num:
            print("恭喜你第" + str(guess_count) + "次猜对啦！")
            '''guess_count是整数，str和int不能直接相加， 可以用str转换成字符串或者f-string 
            eg:print(f"恭喜你第{guess_count}次猜对啦！")'''
            break
        elif w > num:
            print("猜错啦数字太大啦")
        else:
            print("猜错啦数字太小啦")
    except ValueError:
        print("请输入数字")

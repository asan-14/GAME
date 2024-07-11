# import time

# print("я иду спать")
# time.sleep(12)
# print("я проснулся")

#===================================================


# import random

# random_number = random.randint(0, 100)
# print(random_number)


#===================================================


import random

min_n = 0
max_n = 50
bot_n = random.randint(min_n, max_n)
count_us =10


print(f"Начало игры. Тебе нужно будет угодать число от {min_n} до {max_n}")
bot_n = random.randint(min_n, max_n)

while True:
    if count_us == 0:
        print("К сожалению вы проиграли:(")
        break

    user_ans = int(input(f" У вас {count_us} попыток! Попробуйте угодать число: "))

    if user_ans > bot_n:
        print("Ваше число больше чем загаданное...")
    elif user_ans < bot_n:
        print("Ваше число меньше чем загадонное...")
    elif user_ans == bot_n:
        print("Вы угодали!")
        break

    count_us -=1



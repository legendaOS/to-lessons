n = int(input("Введите число n: "))
k = int(input("Введите число k: "))

if n*k % 22 == 0: #остаток от деление равен нулю только если число делится нацело
    if n*k % 100 == 22: #последние две цифры это 22
        print('ДА')
    else:
        print("НЕТ")
else:
    print("НЕТ")
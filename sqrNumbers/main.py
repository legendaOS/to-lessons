number = int(input("Введите число: "))

res = 1
while res ** 2 <= number:
    print(res ** 2)
    res = res + 1
else:
    print("Вы ввели слишком маленькое число")
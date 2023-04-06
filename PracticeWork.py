def elgam():
    p = 23
    g = 5
    # Секретные параметры
    x = int(input('Введите значение x: '))
    y = pow(g, x, p)
    k = int(input('Введите значение k: '))
    # Сообщение
    m = int(input('Введите значение m: '))
    # Генерация подписи
    a = pow(g, k, p)
    b = (m - x*a) * pow(k, -1, p-1) % (p-1)
    # Проверка
    v1 = pow(g, m, p)
    v2 = pow(y, a, p) * pow(a, b, p) % p
    print("Подпись: ", a,b)
    print("Проверка ЭЦП EG: ", v1 == v2)

def rsa():
    # Открытые ключи
    n = int(input('Введите значение n: '))
    e = int(input('Введите значение e: '))

    # хэш-значение сообщения
    m = int(input('Введите значение m: '))
    s = int(input('Введите значение s: '))

    # проверка ЭЦП
    print("Проверка ЭЦП: ", m == pow(s, e, n))

choice = input('Введите ElGam или RSA учитывая регистр ')
if (choice=="RSA"): rsa()
if (choice=="ElGam"): elgam()
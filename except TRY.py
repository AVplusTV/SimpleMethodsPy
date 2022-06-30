try:
    old = int(input("Введите число: "))
    print("Введенное число:", old)
except:
    while except == True:
        try:
            old = int(input("Введите число: "))
            print("Введенное число:", old)
        except:
            print ("\nВведи уже гребанное число!? =>")
            old = int(input("Введите число: "))
        print ("\nкукукукукук")
old = input("Пока!")
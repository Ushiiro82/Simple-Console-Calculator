def main():
    operations_list = ["+", "-", "*", "/"]

    # Ввод чисел и операции с обработкой исключений
    while True:
        try:
            first_num = float(input("Введите первое число: "))
            sec_num = float(input("Введите второе число: "))
            operation = input("Введите операцию (+, -, *, /): ")

            if operation not in operations_list:
                print("Ошибка: Неверная операция. Пожалуйста, введите одну из операций: +, -, *, /")
                continue

            # Выполнение операции сложения/вычитания/умножения/деления
            if operation == "+":
                print(f"Результат: {first_num + sec_num}")
            elif operation == "-":
                print(f"Результат: {first_num - sec_num}")
            elif operation == "*":
                print(f"Результат: {first_num * sec_num}")
            elif operation == "/":
                if sec_num == 0:
                    print("Ошибка: Деление на ноль невозможно.")
                else:
                    print(f"Результат: {first_num / sec_num}")
            break  # Выход из цикла, если все прошло успешно
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные числа.")


if __name__ == '__main__':
    main()

